"""
Matrix Rank
The rank of a matrix is defined as the maximum number of linearly 
independent row or column vectors in the matrix. It tells you the 
dimension of the vector space spanned by its rows or columns.

Mathematically, for a matrix A, the rank is defined as:
rank(A) = maximum number of linearly independent rows or columns

Use Cases
Determining whether a system of linear equations has a unique solution, infinitely many solutions, or no solution.
Checking if a matrix is invertible (a matrix is invertible if its rank equals its dimension).
Used in data analysis (e.g., Principal Component Analysis) and signal processing.


Explanation
We use NumPy’s np.linalg.matrix_rank() to compute the rank.
The matrix rank is printed along with the input matrix.

Expected Output
Matrix A:
[[1 2 3]
 [4 5 6]
 [7 8 9]]

Rank of A:
2

Notes
If the rank of a matrix is equal to its number of rows (or columns), the matrix has full rank.
If the rank is less than the number of rows or columns, the matrix is said to be rank-deficient.

"""

# matrix_rank.py
# Astro Pema Software (c)
# Code by Oba Ozai & ChatGPT4 - 2024-11-14

import numpy as np

def compute_rank(A):
    # Calculate the rank using NumPy's built-in function
    rank = np.linalg.matrix_rank(A)
    return rank

# Example matrix
A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Calculate the rank
rank = compute_rank(A)

print("Matrix A:")
print(A)
print("\nRank of A:")
print(rank)

#EOF matrix_rank.py

