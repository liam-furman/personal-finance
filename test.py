import numpy as np
import pandas as pd

from helper import generate_future_economy_historical

# TODO: Allow random seed to be provided

N_TRIALS = 3
# TODO: Make prediction period a variable based on life expectancy
PERIODS_TO_PREDICT = 60*12 # 60 years

#### Personal finance parameters
STARTING_EQUITY_BALANCE = 1e5
STARTING_MONTHLY_EXPENSES = 1E2
STARTING_NET_SALARY = 3E3
PERIODS_TO_RETIREMENT = 35*12

historical_index = pd.date_range(start = '1923-01-01', end = '2023-01-01', freq = 'M')
n_historical_periods = len(historical_index)
historical_economy = pd.DataFrame({
    'year': historical_index.year,
    'month': historical_index.month,
    # random returns + inflation for testing
    'equity_returns': np.random.uniform(-0.12, 0.12, size = n_historical_periods),
    'inflation': np.random.uniform(0, 0.085, size = n_historical_periods),
    # For testing assuming salary increase is the same as inflation
    'salary_increase': np.random.uniform(0, 0.085, size = n_historical_periods),
})

# TODO: investigate whether this can be vectorized
for trial in range(0, N_TRIALS):
    print("Trial:", trial)
    future = generate_future_economy_historical(historical_economy, PERIODS_TO_PREDICT)
    # TODO: Be clearer around balances etc at start vs end period
    for period in range(0, PERIODS_TO_PREDICT):
        future['trial'] = trial
        # TODO: Make sure period is an int
        future.loc[period, ['period']] = period
        if period == 0:
            future.loc[period, ['equity_balance']] = STARTING_EQUITY_BALANCE
            future.loc[period, ['expenses']] = STARTING_MONTHLY_EXPENSES
            future.loc[period, ['net_salary']] = STARTING_NET_SALARY
        else:
            previous_period = period - 1  
            future.loc[period, ['expenses']] = future.expenses[previous_period] * (1 + future.inflation[previous_period])
            if period < PERIODS_TO_RETIREMENT:
                future.loc[period, ['net_salary']] = future.net_salary[previous_period] * (1 + future.salary_increase[previous_period])
            else:
                future.loc[period, ['net_salary']] = 0
            future.loc[period, ['equity_balance']] = future.equity_balance[previous_period] * (1 + future.equity_returns[previous_period]) + future.net_salary[previous_period] - future.expenses[previous_period]
    if trial == 0:
        futures = future
    else:
        futures = pd.concat([futures, future])
futures['failed'] = future.equity_balance < future.expenses

pd.set_option('display.max_rows', 5000)
print(futures)

