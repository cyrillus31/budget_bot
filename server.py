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
    my_budget.spent = int(await db.get_this_month_expenses())
    my_budget.monthly_goal = int(await db.get_monthly_limit())
    my_budget.days = calendar.days_left()

    update_id = json.loads(requests.get(url+"/getUpdates").text)["result"][-1]["update_id"]
    time.sleep(0.4)
    last_update_id = update_id

    while True:
        async with aiohttp.ClientSession() as session:
            message, update_id = await getUpdates(session)
            # print(message, update_id)

            answer = message_handler(update_id, last_update_id, message)

            # if there is an answer - send message to the user
            if isinstance(answer, str) and answer != "":
                sendMessage(session, answer)

            last_update_id = update_id
            time.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
