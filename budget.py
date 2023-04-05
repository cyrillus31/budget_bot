"This module deals with internal budget logic"


class Budget():
    """This class """

    def __init__(self):
        self.daily_limit = 0
        self.spent = 0
        self.monthly_goal = 60000
        self.days_left = 30

    def update_monthly_limit(self, new_goal):
        "Updates monthly limit"
        self.monthly_goal = new_goal

    def update_days_in_month(self, days_in_month):
        "Updates amount of days left"
        self.days_left = days_in_month

    def update_daily_limit(self):
        "Updates the value of daily limit"
        self.daily_limit = (self.monthly_goal - self.spent) / self.days_left

    def status(self):
        """This method reterns the current status of the budget"""
        return f"""Your current limit for today is {round(self.daily_limit, 2)} \n
This month you've spent {self.spent} out of {self.monthly_goal}. 
There are {self.days_left} days left in the current month."""

    def update_spendings(self, spent, category="other"):
        "Updates spendings"
        if category != "0":
            self.spent += spent
