#!/usr/bin/python3
"""Module 0-rotate_2d_matrix"""


def rotate_2d_matrix(matrix):
    """
    rotates a n x n 2D matrix 90 degrees clockwise
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            """prints [[1, 4, 7], [2, 5, 8], [3, 6, 9]]"""

    """reverse"""
    for i in range(len(matrix)):
        matrix[i].reverse()
