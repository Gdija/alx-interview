#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n):
    """function to return the minimum operations of copy and paste"""
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    else:
        for i in range(n//2, 0, -1):
            """find the largest divisor"""
            if n % i == 0:
                return minOperations(i) + n//i
