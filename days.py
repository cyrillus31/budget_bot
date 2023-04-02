from datetime import datetime

tday = datetime.now().date()
new_month = datetime(tday.year, tday.month+1, 1).date()
# print(tday)
# print(new_month)
# how many days left to the end of the month
print((new_month-tday).days)
