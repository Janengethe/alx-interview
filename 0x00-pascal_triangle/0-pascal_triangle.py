#!/usr/bin/python3

from math import factorial


"""
Module 0-pascal_triangle
"""


def nCr(n, r):
    """
    returns factorial
    """
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


def pascal_triangle(n):
    """
    Returns pascal's trangle(list of lists of integers)
    or an empty list if n <= 0
    """
    plist = []
    for i in range(n):
        plist.append((list((nCr(i, j) for j in range(0, i + 1)))))
    return plist
