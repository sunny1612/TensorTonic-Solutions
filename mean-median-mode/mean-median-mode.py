from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    x.sort()
    ct = 1
    maxct = 1
    prev = x[0]
    mode = x[0]
    s = x[0]
    N = len(x)
    for num in x[1:]:
        if num == prev:
            ct += 1
        else:
            if ct > maxct:
                maxct = ct
                mode = prev
            else:
                ct = 1
                prev = num
        s += num
    if ct > maxct:
        mode = num
    mean = s * 1.0 / N
    if N % 2 == 0: 
        median = (x[N//2 - 1] + x[N//2]) * 1.0 / 2.0
    else:
        median = x[N // 2] * 1.0
    return {"mean": mean, "median": median, "mode": mode * 1.0}