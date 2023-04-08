# import aiohttp
import asyncio
import json

class Connection():
    
    url = "https://api.telegram.org/bot"

    def __init__(self, token: str, aiohttp_session):
        self.session = aiohttp_session
        self.url = Connection.url+token
    

    async def get_updates(self, offset, limit, timeout):
        pass


    async def send_message(self, chat_id, text):
        "Sends a message back"

        payload = {'text': text, 'chat_id': chat_id}
        await self.session.post(self.url+"/sendMessage", json=payload)
        print('message sent')
    





