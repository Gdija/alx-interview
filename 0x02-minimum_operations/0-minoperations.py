#!/usr/bin/python3
def minOperations(n):
    """function to return the minimum operations of copy and paste"""
    if n == 1:
        return 0
    for i in range(n//2, 0, -1):
        """find the largest divisor"""
        if n % i == 0:
            return minOperations(i) + n//i
