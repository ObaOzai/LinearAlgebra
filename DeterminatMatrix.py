"""

Determinant of a Matrix

Overview
The determinant is a scalar value that can be computed from the elements of a square matrix.
The determinant is denoted as 
det(A) or ∣A∣.
Determinants are used to:
Determine whether a matrix is invertible.
Solve systems of linear equations using Cramer's Rule.
Calculate areas, volumes, and properties in geometry.

Properties of the Determinant: det(A)=0 implies that the matrix A is singular (non-invertible).

The determinant of the identity matrix is 1.

Explanation of the Code
Matrix Definition:
We define both a 2×2 and a 3×3 matrix using numpy.array().
Determinant Calculation:
The function calculate_determinant() uses np.linalg.det() to compute the determinant.
Running the Program:
The main block defines sample matrices, calculates their determinants, and prints the results.

Output
2x2 Matrix A:
[[4 3]
 [6 3]]
Determinant of 2x2 matrix: -6.0000

3x3 Matrix A:
[[ 6  1  1]
 [ 4 -2  5]
 [ 2  8  7]]
Determinant of 3x3 matrix: -306.0000

"""

# Determinant of a Matrix
# Astro Pema Software (c)
# Oba Ozai Nov 2024

import numpy as np

def calculate_determinant(matrix):
    """
    Calculate the determinant of a matrix.
    """
    return np.linalg.det(matrix)

if __name__ == "__main__":
    # Define a 2x2 matrix
    #A_2x2 = np.array([[4, 3], [6, 3]])
    A_2x2 = np.random.randint(0, 200, size=(2, 2))
    print("2x2 Matrix A:")
    print(A_2x2)
    det_2x2 = calculate_determinant(A_2x2)
    print(f"Determinant of 2x2 matrix: {det_2x2:.4f}")
    
    # Define a 3x3 matrix
    #A_3x3 = np.array([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
    A_3x3 = np.random.randint(0, 200, size=(3, 3))
    print("\n3x3 Matrix A:")
    print(A_3x3)
    det_3x3 = calculate_determinant(A_3x3)
    print(f"Determinant of 3x3 matrix: {det_3x3:.4f}")

# EOF




