#!/usr/bin/python3
"""
Determines the fewest number of coins needed to meet a given total amount
"""

def makeChange(coins, total):
    """
    Returns the fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin value
    for coin in coins:
        # Update dp array for each possible amount
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
