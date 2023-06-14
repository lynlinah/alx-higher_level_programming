#!/usr/bin/python3
#0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix."""
    current_matrix = matrix.copy()
    
    for j in range(len(matrix)):
        current_matrix[j] = list(map(lambda x: x**2, matrix[j]))

        return (current_matrix)
