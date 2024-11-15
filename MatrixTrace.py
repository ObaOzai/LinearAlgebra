"""
# Astro Pema Software (c)
# Code by Oba Ozai

Matrix Trace

The trace of a square matrix is simply the sum of its diagonal elements. For a matrix 
A, the trace is defined as:

trace(A) = ∑ A[i, i] for i = 1 to n

"""
 

import numpy as np

def matrix_trace(matrix):
    # Ensure the matrix is square
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix must be square")
    
    trace = sum(matrix[i][i] for i in range(len(matrix)))
    return trace

# Example matrix
A = [
    [4, 2, 1],
    [0, 5, 7],
    [6, 3, 8]
]

print("Matrix A:")
for row in A:
    print(row)

# Calculate the trace
trace_result = matrix_trace(A)
print(f"\nTrace of the matrix A: {trace_result}")
