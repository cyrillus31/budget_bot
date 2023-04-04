import aiohttp
import json
import asyncio
import os
from budget import Budget
import db
from days import Calendar

TOKEN = os.getenv("BUDGET_TELEBOT_TOKEN").strip()
CHAT_ID = os.getenv("BUDGET_TELEBOT_CHAT_ID").strip()
url = f"https://api.telegram.org/bot{TOKEN}"

# print(requests.get(url+"/getMe").text)


async def getMe(session):
    response = await session.get(url+"/getMe")
    print(response.status)
    print(await response.text())


async def getUpdates(session, offset=0, limit=100) -> str:
    "Rerturns a string of the last recieved message"
    response = await session.get(url+f"/getUpdates?offset={offset}&limit={limit}&allowed_updates=['text']")
    text = await response.text()
    dictionary = json.loads(text)
    message = dictionary["result"][-1]["message"]["text"]
    update_id = dictionary["result"][-1]["update_id"]
    print(message, update_id)
    return message, update_id


async def sendMessage(session, text, chat_it=CHAT_ID):
    "Sends a message back"
    await session.get(url+f"/sendMessage?chat_id={chat_it}&text={text}")
    print("message sent")


async def main():
    "The main function"
    
    last_update = 0

    while True:
        async with aiohttp.ClientSession() as session:
            # await getMe(session)
            message, update_id = await getUpdates(session)
            if update_id != last_update  and message == "hi":
                await sendMessage(session, "PRIVET THERE!")
                last_update = update_id
        await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
