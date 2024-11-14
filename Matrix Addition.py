"""

Matrix addition and subtraction involve element-wise operations on two matrices of the same dimensions.
Given two matrices 

A and B of size m×n, the result C is another matrix where each element is given by:
C [i,j]  = A[i,j] + B{i,j]

Explanation of the Code

Defining Matrices:
We define two matrices, 
A and B, using numpy.array().

Matrix Addition Function:
The function matrix_addition() adds two matrices element-wise.
It checks if the matrices have the same dimensions before adding them.

Matrix Subtraction Function:
The function matrix_subtraction() subtracts one matrix from another element-wise.
It also checks if the matrices have the same dimensions.

Running the Program:
The main block defines two sample matrices and performs both addition and subtraction.

Output
Matrix A:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Matrix B:
[[9 8 7]
 [6 5 4]
 [3 2 1]]

Matrix Addition (A + B):
[[10 10 10]
 [10 10 10]
 [10 10 10]]

Matrix Subtraction (A - B):
[[-8 -6 -4]
 [-2  0  2]
 [ 4  6  8]]

"""

# Matrix Addition and Subtraction
# Astro Pema Software (c)
# Oba Ozai Nov 2024

import numpy as np

def matrix_addition(A, B):
    """
    Perform matrix addition.
    """
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same dimensions for addition.")
    return A + B

def matrix_subtraction(A, B):
    """
    Perform matrix subtraction.
    """
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same dimensions for subtraction.")
    return A - B

if __name__ == "__main__":
    # Define two matrices
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    
    print("Matrix A:")
    print(A)
    print("\nMatrix B:")
    print(B)
    
    # Perform matrix addition
    print("\nMatrix Addition (A + B):")
    C_add = matrix_addition(A, B)
    print(C_add)
    
    # Perform matrix subtraction
    print("\nMatrix Subtraction (A - B):")
    C_sub = matrix_subtraction(A, B)
    print(C_sub)

# EOF


​	
 
