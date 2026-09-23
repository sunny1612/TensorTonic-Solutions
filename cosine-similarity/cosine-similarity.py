import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    d = dot(a, b)
    n1, n2 = norm(a), norm(b)
    if n1 == 0 or n2 == 0:
        return 0.0
    return d / (n1 * n2)

def dot(a: list, b: list) -> float:
    return sum(map(lambda x: x[0] * x[1], zip(a, b)))

import math
def norm(a: list) -> float:
    return math.sqrt(sum(map(lambda x : x * x, a)))