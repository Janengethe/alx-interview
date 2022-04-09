#!/usr/bin/python3

"""
Module 0-pascal_triangle
"""


def factorial(n):
    """factorial of n"""
    fact = 1
    if n == 0 and n == 1:
        return 1
    if n < 0:
        raise ValueError("No factorial of a negative number")
    for i in range(1, n + 1):
        fact = fact * i
    return fact


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
