from arch.bootstrap import StationaryBootstrap

def generate_future_economies_stationary_bootstrap(history):
    """
    Use the Historical Analysis approach to generate a potential future economy: https://www.kitces.com/blog/monte-carlo-models-simulation-forecast-error-brier-score-retirement-planning/
    
    See:
        * https://portfoliooptimizer.io/blog/bootstrap-simulation-with-portfolio-optimizer-usage-for-financial-planning/
    """
    return StationaryBootstrap(
        block_size = 3.15 * len(history) ** (1/3),
        economy = history
    )
    
    