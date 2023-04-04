import aiohttp
import json
import asyncio
import os
from budget import Budget
import db
from days import Calendar

TOKEN = os.getenv("BUDGET_TELEBOT_TOKEN").strip()
url = f"https://api.telegram.org/bot{TOKEN}"

# print(requests.get(url+"/getMe").text)


async def getMe(session):
    response = await session.get(url+"/getMe")
    print(response.status)
    print(await response.text())


async def getUpdates(session):
    response = await session.get(url+"/getUpdates?limit=3")
    text = await response.text()
    dictionary = json.loads(text)
    print(dictionary["result"])


async def main():
    "The main function"
    async with aiohttp.ClientSession() as session:
        # await getMe(session)
        await getUpdates(session)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
