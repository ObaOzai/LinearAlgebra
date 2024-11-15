"""
LU Decomposition
The LU Decomposition is a method of breaking down a square matrix A into two matrices:

L: A lower triangular matrix (all elements above the diagonal are zero).
U: An upper triangular matrix (all elements below the diagonal are zero).
We can express this as:
A = L * U

This decomposition is useful for solving systems of 
linear equations, inverting matrices, and computing determinants.

Mathematical Description in Python-Style Notation
We want to decompose matrix A into matrices L and U. For a matrix of size n x n:
A[i, j] = L[i, j] * U[j, j] for i, j in range(n)

For elements in L, if i < j, then L[i, j] = 0.
For elements in U, if i > j, then U[i, j] = 0.

"""


# lu_decomposition.py
# Astro Pema Software (c)
# Code by Oba Ozai 2024-11-14

import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    # Decomposing matrix A into L and U
    for i in range(n):
        # Upper triangular matrix U
        for j in range(i, n):
            U[i, j] = A[i, j] - sum(L[i, k] * U[k, j] for k in range(i))
        
        # Lower triangular matrix L
        for j in range(i, n):
            if i == j:
                L[i, j] = 1  # Diagonal elements of L are set to 1
            else:
                L[j, i] = (A[j, i] - sum(L[j, k] * U[k, i] for k in range(i))) / U[i, i]
    
    return L, U

# Example matrix
A = np.array([
    [4, 3, 2],
    [2, 1, 1],
    [6, 5, 3]
])

L, U = lu_decomposition(A)

print("Matrix A:")
print(A)
print("\nLower Triangular Matrix L:")
print(L)
print("\nUpper Triangular Matrix U:")
print(U)

#EOF lu_decomposition.py

