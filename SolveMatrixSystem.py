"""
SolveMatrixSystem.py
new version to take care of most situations

Scalable: Handles any size of square matrix, from simple 2x2 systems to more complex ones like 5x5.
Robust Error Handling: Ensures the user inputs the correct data, making it less prone to errors.
Powerful Explanations: Provides detailed analysis of whether a system has infinite solutions, no solution, or a unique solution.
Graphical Visualization: Supports visualizing 2x2 systems (lines) and 3x3 systems (planes).
Extensible: Easily extendable to handle even more complex cases, if needed.

"""

# Astro Pema Software (c) 2024-25
# Code Oba Ozai 

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib

# Ensure correct backend is used for macOS
matplotlib.use('TkAgg')

def calculate_determinant(matrix):
    """Calculate the determinant of a matrix."""
    return np.linalg.det(matrix)

def is_invertible(matrix, epsilon=1e-10):
    """Check if a matrix is invertible."""
    det = calculate_determinant(matrix)
    return abs(det) > epsilon, det

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

def solve_linear_system(A, B):
    """Solve the system A * X = B using NumPy."""
    try:
        return np.linalg.solve(A, B)
    except np.linalg.LinAlgError:
        return None

def analyze_singular_matrix(A, B):
    """Determine if a singular matrix has infinite solutions or no solutions."""
    augmented_matrix = np.column_stack((A, B))
    rank_A = np.linalg.matrix_rank(A)
    rank_augmented = np.linalg.matrix_rank(augmented_matrix)
    
    if rank_A == rank_augmented:
        return "Singular matrix with infinite solutions (dependent equations)."
    else:
        return "Singular matrix with no solution (contradictory equations)."

def plot_solution_2x2(A, B, solution):
    """Plot the solution for a 2x2 system as intersecting lines."""
    x = np.linspace(-10, 10, 400)
    plt.figure()

    for i in range(2):
        a, b = A[i]
        c = B[i]
        if b != 0:
            y = (c - a * x) / b
            plt.plot(x, y, label=f'Line {i+1}: {a}x + {b}y = {c}')
        else:
            plt.axvline(x=c/a, color='red', linestyle='--')
    
    if solution is not None:
        plt.scatter(solution[0], solution[1], color='green', label=f'Solution: ({solution[0]:.2f}, {solution[1]:.2f})', zorder=5)

    plt.axhline(0, color='gray')
    plt.axvline(0, color='gray')
    plt.title('Solution of 2x2 Linear System')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_solution_3x3(A, B, solution):
    """Plot the solution for a 3x3 system as intersecting planes."""
    print("\nGenerating 3D plot for 3x3 system...")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y = np.meshgrid(range(-10, 10), range(-10, 10))

    for i in range(3):
        a, b, c = A[i]
        d = B[i]
        if c != 0:
            z = (d - a * x - b * y) / c
            ax.plot_surface(x, y, z, alpha=0.6)

    if solution is not None:
        ax.scatter(solution[0], solution[1], solution[2], color='red', s=100, label=f'Solution: ({solution[0]:.2f}, {solution[1]:.2f}, {solution[2]:.2f})')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Solution of 3x3 Linear System')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    n = int(input("Enter the size of the square matrix (e.g., 2, 3, ...): "))
    A = get_user_matrix(n)
    B = get_result_vector(n)

    invertible, det = is_invertible(A)
    print(f"\nDeterminant = {det:.4f}")

    if invertible:
        solution = solve_linear_system(A, B)
        if solution is not None:
            print("\nSolution Vector X:")
            print(solution)
            if n == 2:
                plot_solution_2x2(A, B, solution)
            elif n == 3:
                plot_solution_3x3(A, B, solution)
        else:
            print("The system has no unique solution.")
    else:
        explanation = analyze_singular_matrix(A, B)
        print("The matrix is not invertible.")
        print(explanation)
    
    if n > 3:
        print(f"Visualization for {n}x{n} matrices is not supported yet.")
#EOF 






