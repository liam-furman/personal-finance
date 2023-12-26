from arch.bootstrap import StationaryBootstrap

def generate(generator, reps, **kwargs):
    # all series to boostrap must be of the same length
    series_lengths = [len(series) for series in kwargs.values()]
    if len(set(series_lengths)) > 1:
        raise ValueError("All series for boostrapping must be the same length")
    return generator(series_lengths[0], reps, **kwargs)

def stationary_bootstrap(series_length, reps, **kwargs):
    """
    Use the Historical Analysis approach to generate a potential future economy: https://www.kitces.com/blog/monte-carlo-models-simulation-forecast-error-brier-score-retirement-planning/
    
    See:
        * https://portfoliooptimizer.io/blog/bootstrap-simulation-with-portfolio-optimizer-usage-for-financial-planning/
    """
    return StationaryBootstrap(
        # TODO: Experiment with different approaches to choosing block size
        block_size = 3.15 * series_length ** (1/3),
        **kwargs
    ).bootstrap(reps)
    
    