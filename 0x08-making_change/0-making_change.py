#!/usr/bin/python3
"""
determine the fewest number of coins needed to meet a given amount total
"""


def makeChange(coins, total):
    """ function to make changes"""
    if (total == 0):
        return 0
    elif (!total):
        return -1
