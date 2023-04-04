"This module deals with issue of calculating amout of days left"

from datetime import datetime


class Calendar():
    "Deals with dates"
    def __init__(self):
        self.is_new_month = True
        self.tday = datetime.now()

    def update_date(self):
        "Updates today's datetime"
        self.tday = datetime.now()

    def days_left(self):
        "Calculates how many days left in a current month"
        self.next_month = datetime(self.tday.year, self.tday.month+1, 1)

        # how many days left to the end of the month
        return (self.next_month-self.tday).days

    def is_new_month(self) -> bool:
        "Checks if new month has started"
        if self.tday.month != datetime.now().month:
            return True
        return False
