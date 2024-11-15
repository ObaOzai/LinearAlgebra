"""

Matrix Transpose
Overview
Matrix transpose involves flipping a matrix over its diagonal, turning rows into columns and vice versa.
Given a matrix 

A of size m×n, its transpose 
AT will have the size n×m.
Mathematically:
(AT)[i.j] = A[j,i]

​	
 
Applications:
Data preprocessing: Transposing data matrices to switch between observations and features.
Machine learning: Calculating covariance matrices, adjusting input shapes for algorithms.
Computer graphics: Performing transformations and manipulating coordinates.

Explanation of the Code
Matrix Definition:
We define a 2×3 matrix using numpy.array().
Transpose Function:
The function transpose_matrix() uses matrix.T to calculate the transpose of the matrix.
Running the Program:
The main block defines a sample matrix, transposes it, and prints the results.

output

Original Matrix A:
[[1 2 3]
 [4 5 6]]

Transpose of Matrix A (A^T):
[[1 4]
 [2 5]
 [3 6]]

"""

# Matrix Transpose
# Astro Pema Software (c)
# Oba Ozai Nov 2024

import numpy as np

def transpose_matrix(matrix):
    """
    Calculate the transpose of a matrix.
    """
    return matrix.T

if __name__ == "__main__":
    # Define a matrix
    A = np.array([[1, 2, 3], [4, 5, 6]])
    
    print("Original Matrix A:")
    print(A)
    
    # Perform the transpose
    A_transpose = transpose_matrix(A)
    
    print("\nTranspose of Matrix A (A^T):")
    print(A_transpose)

# EOF





