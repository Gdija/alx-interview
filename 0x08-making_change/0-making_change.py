#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    if (total == 0):
        return 0
    else if (!total):
        return -1
