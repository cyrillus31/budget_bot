"This module works with business logic"

from budget import Budget

my_budget = Budget()
my_budget.update_spendings(1000)
my_budget.update_spendings(1000)
my_budget.update_daily_limit()
print(my_budget.status())
