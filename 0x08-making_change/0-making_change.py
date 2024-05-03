#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """"
    Calculate the fewest number of coins needed to make change for the given total amount.

    Parameters:
        coins (list of int): A list of coin denominations.
        total (int): The total amount for which to make change.

    Returns:
        int: The fewest number of coins needed to make change for the given total amount.
            Returns -1 if it's not possible to make change for the total amount.
    """
    if (total == 0):
        return 0
    elif (!total):
        return -1
