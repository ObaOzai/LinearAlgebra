"""
Scalar Multiplication
Overview
Scalar multiplication involves multiplying each element of a matrix by a scalar value.
Given a matrix 

A of size m×n and a scalar k, the result is another matrix B where each element is given by:
B[i,j] = k × A[i,j] 

​	
 
Applications: Scaling operations in graphics, data normalization, and transformations.

Explanation of the Code
Matrix Definition:
We define a 3×3 matrix A using numpy.array().

Scalar Multiplication Function:
The function scalar_multiplication() multiplies each element of the matrix by the scalar using the expression scalar * matrix.

Running the Program:
The main block defines a sample matrix A and a scalar k, performs the multiplication, and prints the result.

Output
Matrix A:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Scalar: 3

Scalar Multiplication (k * A):
[[ 3  6  9]
 [12 15 18]
 [21 24 27]]

"""

# Scalar Multiplication of a Matrix
# Astro Pema Software (c)
# Oba Ozai  Nov 2024

import numpy as np

def scalar_multiplication(matrix, scalar):
    """
    Perform scalar multiplication on a matrix.
    """
    return scalar * matrix

if __name__ == "__main__":
    # Define a matrix
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    # Define a scalar value
    k = 3
    
    print("Matrix A:")
    print(A)
    print(f"\nScalar: {k}")
    
    # Perform scalar multiplication
    print("\nScalar Multiplication (k * A):")
    B = scalar_multiplication(A, k)
    print(B)

# EOF


