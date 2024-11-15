"""
QR Decomposition
QR Decomposition is a method of decomposing a matrix A into two matrices:
A = Q * R

Where:

Q is an orthogonal matrix (i.e., its columns are orthonormal).
R is an upper triangular matrix.

Use Cases
Solving systems of linear equations.
Least squares optimization problems.
Eigenvalue computations.
Numerical analysis and solving linear regression.

Explanation
We use NumPy’s np.linalg.qr() function to compute the QR decomposition.
The matrix A is decomposed into two matrices: Q (orthogonal) and R (upper triangular).
We print both Q and R to verify the decomposition.

Expected Output
Matrix A:
[[ 12 -51   4]
 [  6 167 -68]
 [ -4  24 -41]]

Orthogonal Matrix Q:
[[-0.85714286  0.39428571  0.33142857]
 [-0.42857143 -0.90285714 -0.03428571]
 [ 0.28571429 -0.17142857  0.94285714]]

Upper Triangular Matrix R:
[[-14.  21. -14.]
 [  0. 175. -70.]
 [  0.   0.  35.]]

Notes
QR decomposition is often used in numerical methods to solve systems of linear equations and to compute eigenvalues.
The orthogonality of Q implies that Qᵀ * Q = I, where I is the identity matrix.

"""

# qr_decomposition.py
# Astro Pema Software (c)
# Code by Oba Ozai - 2024-11-14

import numpy as np

def perform_qr_decomposition(A):
    # Perform QR Decomposition using NumPy
    Q, R = np.linalg.qr(A)
    return Q, R

# Example matrix
A = np.array([
    [12, -51, 4],
    [6, 167, -68],
    [-4, 24, -41]
])

# Perform QR Decomposition
Q, R = perform_qr_decomposition(A)

print("Matrix A:")
print(A)
print("\nOrthogonal Matrix Q:")
print(Q)
print("\nUpper Triangular Matrix R:")
print(R)

#EOF qr_decomposition.py



