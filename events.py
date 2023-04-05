import db

# def help_message_handler(update_id, last_update, message) -> str:
    # if update_id != last_update  and message == "hi":
        # return "HELLO THERE! NEED SOME  HEEEELP?"


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


async def message_handler(update_id, last_update, message) -> str:
    """It takes update_id, last_update and recieved message 
    and comes back with a string response"""

    # Help message
    if update_id != last_update and message == "/help":
        answer = help_message_handler(update_id, last_update, message)
        return answer

    # Update monthly limit
    elif update_id != last_update  and message == "/monthly_limsit":
        return answer

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

    else:
        return None
