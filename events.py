import db
import json

# def help_message_handler(update_id, last_update, message) -> str:
    # if update_id != last_update  and message == "hi":
        # return "HELLO THERE! NEED SOME  HEEEELP?"


async def getMe(session, url):
    response = await session.get(url+"/getMe")
    print(response.status)
    print(await response.text())


async def getUpdates(session, url, offset=0, limit=100) -> str:
    "Rerturns a string of the last recieved message"
    async with session.get(url+"/getUpdates") as response:
        text = await response.text()
    dictionary = json.loads(text)
    # print(dictionary)
    message = dictionary["result"][-1]["message"]["text"]
    update_id = dictionary["result"][-1]["update_id"]
    return message, update_id


async def sendMessage(session, url, text, chat_it):
    "Sends a message back"
    await session.get(url+f"/sendMessage?chat_id={chat_it}&text={text}")
    print("message sent")


async def message_handler(update_id, last_update, message, budget_class) -> str:
    """It takes update_id, last_update and recieved message 
    and comes back with a string response"""

    # Help message
    if update_id != last_update and ("/help" in message) or ("/start" in message):
        answer = "use following functions: /help /start /status /monthly_limit_upd /monthly_limit_ins"
        return answer

    # Update monthly limit
    elif update_id != last_update and "/monthly_limit_upd" in message:
        if len(message.split()) == 1:
            return str(budget_class.monthly_goal)
        else:
            new_limit = message.split()[-1]
            budget_class.update_monthly_limit(db.update_monthly_limit(new_limit))
            budget_class.update_daily_limit()
            return "Monthly limit was updated"


    # Insert monthly limit
    elif update_id != last_update and "/monthly_limit_ins" in message:
        if len(message.split()) == 1:
            return str(budget_class.monthly_goal)
        else:
            new_limit = message.split()[-1]
            budget_class.update_monthly_limit(db.insert_monthly_limit(new_limit))
            budget_class.update_daily_limit()
            return "Monthly limit was created"


    # Status message
    elif update_id != last_update  and message == "/status":
        budget_class.update_daily_limit()
        return budget_class.status()

    # Adding expenses
    elif update_id != last_update:
        try:
            expense = message.split()[0]
            expense = int(expense)
            category = message.split()[-1]
            budget_class.update_spendings(db.insert_expenses(expense, category), category)
            budget_class.update_daily_limit()
            return "Spendings added"

        except ValueError:
            return "I don't understand you"

    else:
        return None
