import random

def generate_future_economy_historical(history, period):
    """
    Use the Historical Analysis approach to generate a potential future economy: https://www.kitces.com/blog/monte-carlo-models-simulation-forecast-error-brier-score-retirement-planning/
    """

    start_index = random.randint(0, history.shape[0] - period)
    return history.iloc[start_index: start_index + period].reset_index(drop=True).drop(columns=['year', 'month'])