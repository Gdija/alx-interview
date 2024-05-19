#!/usr/bin/python3

"""determine the winner of the prime number game"""


def isWinner(x, nums):

    """
    winner function based on number of rounds and array of n
    x  is the number of rounds
    nums array
    """
    def prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    n = max(nums)
    dp = [False] * (n + 1)
    dp[0] = False

    for i in range(1, n + 1):
        if prime(i):
            dp[i] = True
            for j in range(1, i):
                if prime(j):
                    dp[i] &= dp[i - j]

    maria_wins = sum(dp[i] for i in nums)
    ben_wins = x - maria_wins

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
