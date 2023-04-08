from telegram_bot_api import Connection
import aiohttp
import asyncio
import os

TOKEN = os.getenv("BUDGET_TELEBOT_TOKEN").strip()
CHAT_ID = os.getenv("BUDGET_TELEBOT_CHAT_ID").strip()


async def main():
    async with aiohttp.ClientSession() as session:
        connection = Connection(TOKEN, session)

        await connection.send_message(CHAT_ID, "hi\nwhat is goin on?")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
