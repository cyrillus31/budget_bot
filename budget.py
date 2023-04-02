"This module deals with internal budget logic"

import datetime
import time


class Budget:
    """This class """
    monthly_goal = 60000
    days = 30

    def __init__(self):
        self.days_left = 30
        self.daily_limit = 0
        self.spent = 0

    def update_daily_limit(self):
        "Updates the value of daily limit"
        self.daily_limit = (Budget.monthly_goal - self.spent) / self.days_left

    def status(self):
        """This method reterns the current status of the budget"""
        return f"""Your current limit for today is {round(self.daily_limit, 2)}
This month you've spent {self.spent} out of {Budget.monthly_goal}"""

    def update_spendings(self, spent, category="other"):
        "Updates spendings"
        if category != "0":
            self.spent += spent
