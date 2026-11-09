import numpy as np

def finite_difference_derivative(coefficients: list, x: float, h: float) -> tuple[float, float, float]:
    """
    Returns the value at x, the value at x plus h, and the estimated slope.
    """
    fx, fxh = coefficients[0] * 1.0, coefficients[0] * 1.0
    px, pxh = 1.0, 1.0
    for i in range(1, len(coefficients)):
        px *= x
        pxh *= (x + h)
        fx += px * coefficients[i]
        fxh += pxh * coefficients[i]
    return (fx, fxh, (fxh - fx) / h)