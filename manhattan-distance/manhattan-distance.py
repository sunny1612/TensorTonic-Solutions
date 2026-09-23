import numpy as np

def manhattan_distance(x: list, y: list) -> float:
    """
    Returns the Manhattan distance as a Python float.
    """
    import math
    return sum(map(lambda x : math.fabs(x[0] - x[1]), zip(x, y)))