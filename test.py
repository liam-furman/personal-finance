import bootstrap
import numpy as np

from dynamics import *

# Fake historical data for testing 
N_HISTORICAL_PERIODS = 12 * 100
HISTORICAL_EQUITY_RETURNS = np.random.uniform(0.08, 0.12, size = N_HISTORICAL_PERIODS)
HISTORICAL_INFLATION = np.random.uniform(0, 0.05, size = N_HISTORICAL_PERIODS)

# Simulation
N_REPS = 3
N_SIM_PERIODS = 30*12
TIME_STEP = 1.0 / 12

# Initial values for testing
STARTING_EQUITY = 1e5
STARTING_EXPENSES = 1E2
STARTING_NET_SALARY = 3E3
STARTING_AGE = 36

# Financial plan parameters
RETIREMENT_AGE = 65

future_economies = bootstrap.generate(
    bootstrap.stationary_bootstrap, reps=100,
    equity_returns=HISTORICAL_EQUITY_RETURNS,
    inflation = HISTORICAL_INFLATION
)

for rep in range(N_REPS):
    print(">>>>>>> rep:", rep)
    economy = next(future_economies)
    expenses = STARTING_EXPENSES
    equity = STARTING_EQUITY
    salary = STARTING_NET_SALARY
    age = STARTING_AGE
    for inflation, equity_returns in zip(economy[1]['inflation'],economy[1]['equity_returns'] ):
        print(">> Step")
        age = update_age(age, TIME_STEP)
        salary = update_salary(salary, inflation, age, RETIREMENT_AGE)
        expenses = update_expenses(expenses, inflation)
        surplus = update_surplus(salary, expenses)
        equity = update_equities(equity, equity_returns, surplus)
        print("Age:", age)
        print("salary:", salary)
        print("expenses:", expenses)
        print("surplus:", surplus)
        print("inflation:", inflation)
        print("equity_return:", equity_returns)
        print("Equity:", equity)