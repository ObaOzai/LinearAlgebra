"""
Singular Value Decomposition
Singular Value Decomposition (SVD) is a method of decomposing a matrix into three other matrices:
A = U * Σ * Vᵀ

Where:

U is an orthogonal matrix.
Σ (Sigma) is a diagonal matrix containing the singular values.
Vᵀ (V transpose) is an orthogonal matrix.

Use Cases
Data compression (e.g., image compression).
Noise reduction in signal processing.
Used in Principal Component Analysis (PCA) for dimensionality reduction.
Solving systems of linear equations, particularly when the system is overdetermined.

Explanation
We use NumPy’s np.linalg.svd() function to perform SVD.
The matrix A is decomposed into three matrices: U, Σ, and Vᵀ.
We print each of the components to understand how A is factorized.

Expected Output

Matrix A:
[[ 3  1  1]
 [-1  3  1]]

U Matrix:
[[-0.85749293  0.51449576]
 [-0.51449576 -0.85749293]]

Sigma (Singular Values):
[3.86432845 2.0382492 ]

V Transpose Matrix (Vᵀ):
[[-0.63245553 -0.31622777 -0.70710678]
 [ 0.77459667 -0.38729833 -0.5       ]
 [-0.         -0.8660254   0.5       ]]

Notes

The singular values in Σ are always non-negative and sorted in descending order.
The columns of U are the left singular vectors, and the rows of Vᵀ are the right singular vectors.
Useful in reducing the dimensionality of data, solving ill-posed systems, and more.

"""

# svd_decomposition.py
# Astro Pema Software (c)
# Code by Oba Ozai  - 2024-11-14

import numpy as np

def perform_svd(A):
    # Perform Singular Value Decomposition
    U, Sigma, Vt = np.linalg.svd(A)
    return U, Sigma, Vt

# Example matrix
A = np.array([
    [3, 1, 1],
    [-1, 3, 1]
])

# Perform SVD
U, Sigma, Vt = perform_svd(A)

print("Matrix A:")
print(A)
print("\nU Matrix:")
print(U)
print("\nSigma (Singular Values):")
print(Sigma)
print("\nV Transpose Matrix (Vᵀ):")
print(Vt)

#EOF svd_decomposition.py


