#!/usr/bin/python3
"""
Module 0-making_change
"""


def makeChange(coins, total):
    """
    returns the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    count = 0
    sorted_coins = sorted(coins, reverse=True)

    for coin in sorted_coins:
        while total >= coin:
            total -= coin
            count += 1

    return count if total == 0 else -1
