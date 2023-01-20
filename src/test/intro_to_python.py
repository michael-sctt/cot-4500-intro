# Michael Scott
# COT4500 Intro Assignment

# Imports
import numpy as np

# Prints matrix, with extra space afterwards
def print_matrix(matrix):
    for row in matrix:
        for val in row:
            print(val, end=' ')
        print()
    print()

if __name__ == "__main__":
    # Initialize matrix
    matrix = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

    # Problem 1
    for i in range(0, 3):
        for j in range(0, 3):
            if (i == j):
                matrix[i][j] = 1
    print_matrix(matrix)

    # Problem 2
    for i in range(0, 3):
        for j in range(0, 3):
            if (i != j):
                matrix[i][j] += 3
    print_matrix(matrix)

    # Problem 3
    matrix = np.delete(matrix, 2, 1)
    print_matrix(matrix)
