#!/usr/bin/python3
""" determine the winner of the prime number game """


def isWinner(x, nums):

    """
    x is the number of rounds and nums is an array of n
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    You can assume n and x will not be larger than 10000
    """
    while(x <= len(nums)):
        for n in range(n+1):
