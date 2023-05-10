"""This module decides which actions should be taken depending on the incoming message"""
import db


async def getMe(session, url):
    response = await session.get(url+"/getMe")
    print(response.status)
    print(await response.text())


async def message_handler(message, budget_class) -> str:
    """It takes update_id, last_update and recieved message 
    and comes back with a string response"""

    # Help message
    if ("/help" in message) or ("/start" in message):
        answer = "use following functions: /help /status /monthly_limit_upd /monthly_limit_ins"
        return answer

    # Update monthly limit
    elif "/monthly_limit_upd" in message:
        if len(message.split()) == 1:
            return str(budget_class.monthly_goal)
        else:
            new_limit = message.split()[-1]
            budget_class.update_monthly_limit(db.update_monthly_limit(new_limit))
            budget_class.update_running_daily_limit()
            return "Monthly limit was updated"

    # Insert monthly limit
    elif "/monthly_limit_ins" in message:
        if len(message.split()) == 1:
            return str(budget_class.monthly_goal)
        else:
            new_limit = message.split()[-1]
            budget_class.update_monthly_limit(db.insert_monthly_limit(new_limit))
            budget_class.update_running_daily_limit()
            return "Monthly limit was created"

    # Status message
    elif message == "/status":
        # budget_class.update_running_daily_limit()
        return budget_class.status()

    # Today status message
    elif message == "/today":
        # budget_class.update_running_daily_limit()
        return budget_class.today()

    elif message == "/reset":
        db.reset()
        return "Database was reset"


    # Adding expenses
    else:
        try:
            expense = message.split()[0]
            expense = int(expense)
            category = " ".join(message.split()[1:])
            budget_class.update_spendings(db.insert_expenses(expense, category), category)
            # budget_class.update_running_daily_limit()
            return "Spendings added"

        except ValueError:
            return "I don't understand you"
