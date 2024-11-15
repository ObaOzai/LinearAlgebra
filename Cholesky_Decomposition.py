"""
Cholesky Decomposition

Cholesky Decomposition is a method of decomposing a positive definite
matrix A into the product of a lower triangular matrix L and its transpose:
A = L * Lᵀ

Where:

L is a lower triangular matrix.

Use Cases
Efficiently solving systems of linear equations.
Numerical methods in optimization.
Used in statistical models, such as the covariance matrix in multivariate distributions.
More efficient than LU decomposition for positive definite matrices.

Explanation
We use NumPy’s np.linalg.cholesky() function to compute the Cholesky decomposition.
The matrix A must be positive definite; otherwise, the decomposition is not possible.
We verify the decomposition by checking if L * Lᵀ gives us back the original matrix A.

Matrix A:
[[25 15 -5]
 [15 18  0]
 [-5  0 11]]

Lower Triangular Matrix L:
[[ 5.  0.  0.]
 [ 3.  3.  0.]
 [-1.  1.  3.]]

Verification (L * Lᵀ):
[[25 15 -5]
 [15 18  0]
 [-5  0 11]]

Notes
Cholesky decomposition is faster and more stable than LU decomposition but is limited to positive definite matrices.
Useful in solving linear systems and optimization problems, especially in machine learning and numerical simulations.

"""

# cholesky_decomposition.py
# Astro Pema Software (c)
# Code by Oba Ozai - 2024-11-14

import numpy as np

def perform_cholesky_decomposition(A):
    try:
        # Perform Cholesky Decomposition using NumPy
        L = np.linalg.cholesky(A)
        return L
    except np.linalg.LinAlgError:
        return None

# Example positive definite matrix
A = np.array([
    [25, 15, -5],
    [15, 18,  0],
    [-5,  0, 11]
])

# Perform Cholesky Decomposition
L = perform_cholesky_decomposition(A)

print("Matrix A:")
print(A)

if L is not None:
    print("\nLower Triangular Matrix L:")
    print(L)
    print("\nVerification (L * Lᵀ):")
    print(np.dot(L, L.T))
else:
    print("\nMatrix A is not positive definite and cannot be decomposed.")

#EOF cholesky_decomposition.py


