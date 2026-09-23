import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    return {
        "pmf": np.array(list(map(lambda y: p if y == 1 else 1 - p, x))),
        "mean": float(p),
        "variance": 1.0 * p * (1 - p)
    }