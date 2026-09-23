import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    return sum(map(lambda x: x[0] * x[1], zip(x, y))) * 1.0