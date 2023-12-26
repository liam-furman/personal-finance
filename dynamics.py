def update_equities(prev, returns, surplus):
    new = prev * (1 + returns) + surplus
    if new > 0:
        return new
    else:
        return 0

def update_salary(prev, inflation, age, retirement_age):
    if age < retirement_age:
        return prev * (1 + inflation)
    else:
        return 0
    
def update_expenses(prev, inflation):
    return prev * (1 + inflation)

def update_surplus(income, expenses):
    return income - expenses

def update_age(prev, time_step):
    return prev + time_step