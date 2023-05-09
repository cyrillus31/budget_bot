"This module deals with internal budget logic"


class Budget():
    """This class """

    def __init__(self):
        self.running_daily_limit = 0
        self.spent = 0
        self.monthly_goal = 60000
        self.days_left = 30
        self.days_in_month = 31
        self.daily_limit = 2000
        self.spent_today = 0

    def update_monthly_limit(self, new_goal):
        "Updates monthly limit"
        self.monthly_goal = new_goal

    def update_days_in_month(self, days_in_month):
        "Updates amount of days left"
        self.days_left = days_in_month

    def update_running_daily_limit(self):
        "Updates the value of daily limit"
        if self.days_left == 0:
            self.days_left = 1
        self.running_daily_limit = (self.monthly_goal - self.spent) / self.days_left
        self.daily_limit = self.monthly_goal / self.days_in_month

    def status(self):
        """This method reterns the current status of the budget"""
        return f"""Your your average spending for the ramianing days should not exceed {round(self.running_daily_limit, 2)} per day.\n
This month you've spent {self.spent} out of {self.monthly_goal}. 
There are {self.days_left} days left in the current month."""

    def today(self):
        "This method returns how much money is left for today"
        self.daily_limit = round(self.monthly_goal / self.days_in_month, 2)
        spent_today = round(self.spent_today, 2)
        trl = round((self.days_in_month - self.days_left)*self.daily_limit - self.spent, 2)
        return f"""Today's running limit: {trl}\nYou've spent {spent_today} out of average daily limit {round(self.running_daily_limit, 2)} today. You have {round(self.running_daily_limit - spent_today, 2)} left today.\n
Your at the start of the month your daily limit was {round(self.daily_limit)}."""

    def update_spendings(self, spent, category="other"):
        "Updates spendings"
        if category != "0":
            self.spent += spent
