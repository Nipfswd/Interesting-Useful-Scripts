def matmul(A, B):
    """Matrix multiplication."""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    assert cols_A == rows_B, "Matrix dimensions do not match for multiplication!"

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result 

def transpose(A):
    """Matrix transpose."""
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

def scalar_add(A, scalar):
    """Add a scalar to every element,"""
    return [[x + scalar for x in row] for row in A]