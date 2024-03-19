#!/usr/bin/python3
"""
Defines a function that calculates the minimum number of operations
to achieve a certain number of characters using the given rules.
"""

def minOperations(n):
    """
    Calculates the minimum number of operations to achieve n characters.

    Args:
        n (int): The desired number of characters.

    Returns:
        int: The minimum number of operations needed to achieve n characters.
             Returns 0 if n is impossible to achieve.
    """
    if n == 1:
        return 0
    
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n] if dp[n] != float('inf') else 0

if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
