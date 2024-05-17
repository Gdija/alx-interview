#!/usr/bin/python3
""" determine the winner of the prime number game """


def isWinner(x, nums):
    """ winner function based on number of rounds and array of n """
    while(x <= len(nums)):
        for n in range(n+1):
