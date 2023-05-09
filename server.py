import aiohttp
import asyncio
import os
import time

from budget import Budget
import db
from days import Calendar
from events import message_handler
from c31_telegram_bot_api import Connection

TOKEN = os.getenv("BUDGET_TELEBOT_TOKEN").strip()
CHAT_ID = os.getenv("BUDGET_TELEBOT_CHAT_ID").strip()

# print(requests.get(url+"/getMe").text)

my_budget = Budget()
calendar = Calendar()
connection = Connection(TOKEN)
tday = None


async def main():
    "The main function"
    while True:
        # Initialising the budget object
        calendar.update_date()
        my_budget.spent = int(db.get_this_month_expenses())
        my_budget.monthly_goal = int(db.get_monthly_limit())
        my_budget.days_left = calendar.days_left()
        my_budget.days_in_month = calendar.days_in_month()
        my_budget.spent_today = int(db.get_todays_expenses())
        if calendar.tday != tday:
            my_budget.update_running_daily_limit()
        tday = calendar.tday

        async with aiohttp.ClientSession() as session:
            connection.session = session
            updates = await connection.get_updates()

            for update_id in sorted(updates):
                message = updates[update_id]
                # print(update_id)
                # print(message)

                answer = await message_handler(message, my_budget)

                await connection.send_message(CHAT_ID, answer)

        time.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
