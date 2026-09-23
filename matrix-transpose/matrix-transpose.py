import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    m, n = len(A), len(A[0])
    B = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            B[j][i] = A[i][j]
    return np.array(B)
