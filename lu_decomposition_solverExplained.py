#lu_decomposition_solver

"""
# Astro Pema Software (c) 2024-25
# Code Oba Ozai - Astro Pema Software 

Advantages of LU Decomposition in Real-World Applications

Performance and Efficiency:
In Python, using LU decomposition (lu_factor() and lu_solve() from the scipy library) 
can speed up calculations, especially when you have to solve the system multiple times 
with different result vectors B.

Instead of recalculating everything from scratch each time, LU decomposition lets you reuse the breakdown of your matrix 
A, saving computational resources.

Applications in Data Science and Machine Learning:
When you’re working with data, you often need to fit models or solve systems of equations to find patterns. 

For example:
In linear regression, you’re essentially solving a system where you want to minimize the difference between 
predicted and actual values.
LU decomposition can optimize solving these systems quickly, especially when you’re dealing with large datasets.
Engineering and Physics Simulations:
In fields like engineering, physics, and even finance, you often need to model systems with many interacting variables. 
For instance:

Structural analysis: Solving for forces and stresses in a bridge design.

Electric circuits: Determining voltages and currents in a network of components.
Using Python to set up matrices for these systems and solving them efficiently with LU decomposition 
can significantly speed up simulations.

Imagine you have a dataset where you want to predict the relationship between different factors 
(like sales, weather, and marketing spend). You can represent your data as a matrix:

A = np.array([[1, 2], [3, 4]])
B = np.array([5, 6])

By solving for X using LU decomposition, you can quickly find the best-fit parameters for your model.

Financial Forecasting:
In finance, you might have a system of equations representing different factors affecting your investment portfolio. 
If you want to adjust your investments to maximize returns while minimizing risk, you can represent this system as
 a matrix and solve it efficiently.

Pythons LU decomposition can help you quickly adjust your strategies in response to changing market conditions.

Flexibility:
The standard method (np.linalg.solve()) is great for quick, one-time solutions. But if you have a system where 
A remains constant and only B changes, LU decomposition is far more efficient.
In Python, you can reuse the lu_factor() result and just change the vector B.

lu, piv = lu_factor(A)
X1 = lu_solve((lu, piv), B1)
X2 = lu_solve((lu, piv), B2)

For very large systems (think thousands of variables), LU decomposition can
handle the problem more efficiently than the standard method because it
reduces the amount of repetitive calculations.

Lets say you are designing a system for predicting energy consumption based on
several factors like temperature, time of day, and number of people in a building. Your
system might look something like this in Python:

import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Matrix A (coefficients)
A = np.array([
    [1, 2, 3],
    [4, 2, 1],
    [6, 3, 1]
])

# Different result vectors B (representing different scenarios)
B1 = np.array([10, 15, 25])
B2 = np.array([5, 7, 9])

# Use LU Decomposition
lu, piv = lu_factor(A)
solution1 = lu_solve((lu, piv), B1)
solution2 = lu_solve((lu, piv), B2)

print("Solution for scenario 1:", solution1)
print("Solution for scenario 2:", solution2)

By using LU decomposition, you only need to factorize the matrix 
A once, which is highly efficient if you have multiple scenarios to analyze.

LU decomposition is a powerful tool in any Python toolkit for solving systems of equations efficiently,
is why i made it.

It shines in fields where speed and efficiency matter, like data analysis,
engineering, and financial modeling.

Leveraging Python's powerful libraries (numpy, scipy) allows you to apply these
concepts in real-world scenarios without getting bogged down by complex
mathematical notation.

"""


import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lu, lu_factor, lu_solve
from numpy.linalg import LinAlgError

def get_user_matrix(n):
    """Prompt the user to enter a matrix row by row."""
    print(f"\nPlease enter the values for a {n}x{n} matrix:")
    matrix = []
    for i in range(n):
        while True:
            try:
                row = input(f"Enter row {i + 1} (space-separated values): ").split()
                if len(row) != n:
                    print(f"Error: You must enter exactly {n} values.")
                    continue
                matrix.append([float(x) for x in row])
                break
            except ValueError:
                print("Error: Please enter valid numbers.")
    return np.array(matrix)

def get_result_vector(n):
    """Prompt the user to enter the result vector."""
    print(f"\nPlease enter the values for the result vector (B) of size {n}:")
    while True:
        try:
            vector = input("Enter space-separated values: ").split()
            if len(vector) != n:
                print(f"Error: You must enter exactly {n} values.")
                continue
            return np.array([float(x) for x in vector])
        except ValueError:
            print("Error: Please enter valid numbers.")

def lu_decomposition_solver(A, B):
    """Solve system using LU decomposition."""
    try:
        lu, piv = lu_factor(A)
        solution = lu_solve((lu, piv), B)
        return solution
    except LinAlgError:
        return None

def choose_solver():
    """Allow user to choose between different solving methods."""
    print("\nChoose solving method:")
    print("1. Standard method (using numpy.linalg.solve)")
    print("2. LU Decomposition")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        return 'standard'
    elif choice == '2':
        return 'lu'
    else:
        print("Invalid choice. Defaulting to standard method.")
        return 'standard'

def solve_linear_system(A, B, method='standard'):
    """Solve the system A * X = B using the specified method."""
    if method == 'standard':
        try:
            return np.linalg.solve(A, B)
        except LinAlgError:
            return None
    elif method == 'lu':
        return lu_decomposition_solver(A, B)
    return None

if __name__ == "__main__":
    n = int(input("Enter the size of the square matrix (e.g., 2, 3, ...): "))
    A = get_user_matrix(n)
    B = get_result_vector(n)

    # Choose solving method
    method = choose_solver()

    # Solve the system
    solution = solve_linear_system(A, B, method)
    if solution is not None:
        print("\nSolution Vector X:")
        print(solution)
    else:
        print("The system has no unique solution.")
