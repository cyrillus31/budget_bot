"This module deals with issue of calculating amout of days left"

from datetime import datetime


def days_left():
    "Calculates how many days left in a current month"
    tday = datetime.now().date()
    new_month = datetime(tday.year, tday.month+1, 1).date()

    # how many days left to the end of the month
    return (new_month-tday).days
