#!/usr/bin/python3
""" Rotation of a 2D matrix """


def rotate_2d_matrix(matrix):
    """
    Rotates a n x n 2D matrix 90 degrees clockwise

    Argument:
    matrix: List of lists
    """
    n = len(matrix)
    for x in range(n):
        temp = []
        for y in range((n - 1), -1, -1):
            temp.append(matrix[y][x])
        matrix.append(temp)
    for i in range(n):
        matrix.pop(0)
