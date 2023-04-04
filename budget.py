"This module deals with internal budget logic"


class Budget():
    """This class """
    monthly_goal = 60000
    days = 30
    days_left = 29

    def __init__(self):
        self.daily_limit = 0
        self.spent = 0

    @classmethod
    def update_monthly_limit(cls, new_goal):
        "Updates monthly limit"
        cls.monthly_goal = new_goal

    @classmethod
    def update_days_in_month(cls, days_in_month):
        "Updates amount of days left"
        cls.days_left = days_in_month

    def update_daily_limit(self):
        "Updates the value of daily limit"
        self.daily_limit = (Budget.monthly_goal - self.spent) / Budget.days_left

    def status(self):
        """This method reterns the current status of the budget"""
        return f"""Your current limit for today is {round(self.daily_limit, 2)}
This month you've spent {self.spent} out of {Budget.monthly_goal}"""

    def update_spendings(self, spent, category="other"):
        "Updates spendings"
        if category != "0":
            self.spent += spent
