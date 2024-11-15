"""
Inverse of a Matrix
Overview
The inverse of a matrix is a matrix such that when it is multiplied by the original matrix, 
the result is the identity matrix 

Only square matrices (matrices with the same number of rows and columns) that are non-singular 
(i.e., have a non-zero determinant) have an inverse.

Applications:
Solving systems of linear equations.
Cryptography (e.g., encoding and decoding messages).
Control theory and other engineering fields.

"""

# Inverse of a Matrix
# Astro Pema Software (c)
# Oba Ozai Nov 2024

import numpy as np

def calculate_inverse(matrix):
    """
    Calculate the inverse of a matrix.
    """
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return "Matrix is singular and cannot be inverted."

if __name__ == "__main__":
    # Define a 2x2 matrix
    A_2x2 = np.array([[4, 7], [2, 6]])
    print("2x2 Matrix A:")
    print(A_2x2)
    
    # Calculate the inverse
    A_inv_2x2 = calculate_inverse(A_2x2)
    print("\nInverse of 2x2 Matrix A:")
    print(A_inv_2x2)
    
    # Define a 3x3 matrix
    A_3x3 = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    print("\n3x3 Matrix A:")
    print(A_3x3)
    
    # Calculate the inverse
    A_inv_3x3 = calculate_inverse(A_3x3)
    print("\nInverse of 3x3 Matrix A:")
    print(A_inv_3x3)

# EOF

