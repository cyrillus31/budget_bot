import aiohttp
import requests 
import json
import asyncio
import os
import time

from budget import Budget
import db
from days import Calendar
from events import *

TOKEN = os.getenv("BUDGET_TELEBOT_TOKEN").strip()
CHAT_ID = os.getenv("BUDGET_TELEBOT_CHAT_ID").strip()
url = f"https://api.telegram.org/bot{TOKEN}"

# print(requests.get(url+"/getMe").text)

my_budget = Budget()
calendar = Calendar()


async def main():
    "The main function"

    # Initialising the budget object
    my_budget.spent = int(db.get_this_month_expenses())
    my_budget.monthly_goal = int(db.get_monthly_limit())
    my_budget.days_left = calendar.days_left()
    my_budget.update_daily_limit()

    try:
        update_id = json.loads(requests.get(url+"/getUpdates").text)["result"][-1]["update_id"]
        time.sleep(0.4)
    
    except IndexError:
        update_id = "0"
    
    last_update_id = update_id

    while True:

        my_budget.days_left = calendar.days_left()
        my_budget.update_daily_limit()

        async with aiohttp.ClientSession() as session:
            message, update_id = await getUpdates(session, url)
            # print(message, update_id)

            answer = await message_handler(update_id, last_update_id, message, my_budget)

            # if there is an answer send message to the user
            if isinstance(answer, str) and answer != "":
                await sendMessage(session, url, answer, CHAT_ID)

            last_update_id = update_id
            time.sleep(2)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
