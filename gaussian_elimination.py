"""
Gaussian Elimination
Gaussian elimination is a method used to solve systems of linear equations. 
It involves transforming the system's matrix into an upper triangular form, 
making it easier to solve using back substitution.

Given a system of equations:
Ax = b

Alright, Pema! Moving on to the next one:

Algorithm #11: Solving Systems of Linear Equations (Gaussian Elimination)
Gaussian Elimination
Gaussian elimination is a method used to solve systems of linear equations. It involves transforming the system's matrix into an upper triangular form, making it easier to solve using back substitution.

Given a system of equations:

Ax = b
Where:

A is the matrix of coefficients.
x is the vector of unknowns.
b is the vector of constants.
Steps Involved in Gaussian Elimination
Forward Elimination: Transform the matrix A into an upper triangular form.
Back Substitution: Solve for the variables starting from the last row.

Use
Solving systems of linear equations in various fields, including engineering, physics, and economics.
Used in numerical analysis and computer graphics.

Explanation
Augment the matrix A with vector b.
Perform forward elimination to transform A into an upper triangular form.
Use back substitution to find the solution.

Output
Solution to the system:
[ 2.  3. -1.]

This means
x = 2, y = 3, z = -1

Notes
Gaussian elimination is sensitive to numerical stability. In practice, partial pivoting (as done above) helps reduce errors.
This algorithm is fundamental in linear algebra for solving systems of equations efficiently.

"""

# gaussian_elimination.py
# Astro Pema Software (c)
# Code by Oba Ozai - 2024-11-14

import numpy as np

def gaussian_elimination(A, b):
    n = len(b)
    # Augment matrix A with vector b to form [A|b]
    Ab = np.hstack([A, b.reshape(-1, 1)])
    
    # Forward Elimination
    for i in range(n):
        # Find the pivot row
        max_row = np.argmax(abs(Ab[i:, i])) + i
        Ab[[i, max_row]] = Ab[[max_row, i]]
        
        # Eliminate entries below the pivot
        for j in range(i + 1, n):
            factor = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= factor * Ab[i, i:]
    
    # Back Substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:n])) / Ab[i, i]
    
    return x

# Example system of equations:
# 2x + y - z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3
A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
])

b = np.array([8, -11, -3])

# Solve the system using Gaussian elimination
solution = gaussian_elimination(A, b)

print("Solution to the system:")
print(solution)

#EOF gaussian_elimination.py







