#!/usr/bin/python3
"""Module 0-prime_game"""


def primes(n):
    """
    generate prime numbers
    https://www.geeksforgeeks.org/sieve-of-eratosthenes/
    """
    prime = []
    sieve = [True for i in range(n+1)]
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    determine who the winner of each game is
    """
    maria = ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 != 0:
            maria += 1
        else:
            ben += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"
    else:
        return None
