"""

Overview
Matrix multiplication involves multiplying two matrices to produce a third matrix.
Given two matrices 

A of size m×n and B of size n×p, their product C will have the size m×p.

"""

# Matrix Multiplication
# Astro Pema Software (c)
# Oba Ozai  Nov 2024

import numpy as np

def matrix_multiplication(A, B):
    """
    Perform matrix multiplication.
    """
    if A.shape[1] != B.shape[0]:
        raise ValueError("Number of columns in A must match number of rows in B.")
    return np.dot(A, B)

if __name__ == "__main__":
    # Define two matrices
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[7, 8], [9, 10], [11, 12]])
    
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    
    # Perform matrix multiplication
    print("\nMatrix Multiplication (A * B):")
    C = matrix_multiplication(A, B)
    print(C)

# EOF


