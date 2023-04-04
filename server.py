import aiohttp
import requests 
import json
import asyncio
import os
import time

from budget import Budget
import db
from days import Calendar
from handlers import help_message_handler

TOKEN = os.getenv("BUDGET_TELEBOT_TOKEN").strip()
CHAT_ID = os.getenv("BUDGET_TELEBOT_CHAT_ID").strip()
url = f"https://api.telegram.org/bot{TOKEN}"

# print(requests.get(url+"/getMe").text)

my_budget = Budget()
calendar = Calendar()

async def getMe(session):
    response = await session.get(url+"/getMe")
    print(response.status)
    print(await response.text())


async def getUpdates(session, offset=0, limit=100) -> str:
    "Rerturns a string of the last recieved message"
    async with session.get(url+"/getUpdates") as response:
        text = await response.text()
    dictionary = json.loads(text)
    # print(dictionary)
    message = dictionary["result"][-1]["message"]["text"]
    update_id = dictionary["result"][-1]["update_id"]
    return message, update_id


async def sendMessage(session, text, chat_it=CHAT_ID):
    "Sends a message back"
    await session.get(url+f"/sendMessage?chat_id={chat_it}&text={text}")
    print("message sent")


async def main():
    my_budget.spent = int(await db.get_this_month_expenses())
    my_budget.monthly_goal = int(await db.get_monthly_limit())
    my_budget.days = calendar.days_left()

    "The main function"
    last_update = 0
    update_id = json.loads(requests.get(url+"/getUpdates").text)["result"][-1]["update_id"]
    time.sleep(0.4)
    last_update = update_id


    while True:
        async with aiohttp.ClientSession() as session:
            message, update_id = await getUpdates(session)
            # print(message, update_id)

            # Help message
            if update_id != last_update and message == "/help":
                answer = help_message_handler(update_id, last_update, message)
                await sendMessage(session, answer)

            # Update monthly limit
            elif update_id != last_update  and message == "/monthly_limit":

                await sendMessage(session, today_expenses)

            # Status message
            elif update_id != last_update  and message == "/status":
                today_expenses = await db.get_todays_expenses()
                await sendMessage(session, today_expenses)

            # Adding expenses
            elif update_id != last_update:
                try:
                    expense = message.split()[0]
                    expense = int(expense)
                    category = message.split()[-1]
                    await db.insert_expenses(expense, category)
                    await sendMessage(session, "All done!")

                except ValueError:
                    await sendMessage(session, "I don't understand you")
            
            last_update = update_id
            time.sleep(1)
            
            await asyncio.sleep(1)
            



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
