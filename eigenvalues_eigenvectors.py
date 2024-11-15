"""
Eigenvalues and Eigenvectors
The eigenvalues of a matrix A are scalars that, when multiplied by their corresponding eigenvectors, 
yield the same result as applying the matrix transformation on the eigenvector.

Mathematically:
A * v = λ * v

Where:

A is the matrix.
v is the eigenvector.
λ (lambda) is the eigenvalue.
Use Cases
Eigenvalues and eigenvectors are used in:

Principal Component Analysis (PCA)
Quantum mechanics
Vibrations analysis
Computer vision and machine learning


Explanation
We use np.linalg.eig() to compute the eigenvalues and eigenvectors.
We verify the result by checking that A * v is equal to λ * v.

Output
Matrix A:
[[ 4 -2]
 [ 1  1]]

Eigenvalues of A:
[3. 2.]

Eigenvectors of A:
[[ 0.89442719  0.70710678]
 [ 0.4472136  -0.70710678]]

Check A * v = λ * v for eigenvalue 3.0:
A * v = [2.68328157 1.34164079]
λ * v = [2.68328157 1.34164079]

Check A * v = λ * v for eigenvalue 2.0:
A * v = [-1.41421356 -1.41421356]
λ * v = [-1.41421356 -1.41421356]

"""

# eigenvalues_eigenvectors.py
# Astro Pema Software (c)
# Code by Oba Ozai - 2024-11-14

import numpy as np

def compute_eigen(A):
    # Compute eigenvalues and eigenvectors using NumPy
    eigenvalues, eigenvectors = np.linalg.eig(A)
    return eigenvalues, eigenvectors

# Example matrix
A = np.array([
    [4, -2],
    [1, 1]
])

# Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = compute_eigen(A)

print("Matrix A:")
print(A)
print("\nEigenvalues of A:")
print(eigenvalues)
print("\nEigenvectors of A:")
print(eigenvectors)

# Verify by checking A * v = λ * v
for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    λv = eigenvalues[i] * v
    Av = np.dot(A, v)
    print(f"\nCheck A * v = λ * v for eigenvalue {eigenvalues[i]}:")
    print("A * v =", Av)
    print("λ * v =", λv)

#EOF eigenvalues_eigenvectors.py

