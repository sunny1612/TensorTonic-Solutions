import numpy as np
import math

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a Python float.
    """
    # Write code here
    return math.sqrt(sum(map(lambda x : (x[0] - x[1]) * (x[0] - x[1]), zip(x, y))))