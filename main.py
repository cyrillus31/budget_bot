"""This is the main module"""

import datetime
import time


class Budget:
    """This class """
    monthly_goal = 60000
    days = 30

    def __init__(self,  daily_goal, spent, days_left=1,):
        self.days_left = days_left
        self.spent = spent
        self.daily_goal = (Budget.monthly_goal - spent) / self.days_left

    @classmethod
    def status(cls):
        """This method reters the current status of the budget"""
        return """Your current limit for today is {cls.days}
Your running limit for today is {}"""
