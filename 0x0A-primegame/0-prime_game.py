#!/usr/bin/python3
"""
Prime Game module
"""

def isWinner(x, nums):
    """
    Determine the winner of the prime game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of n values for each round.

    Returns:
        str: Name of the player that won the most rounds (Maria or Ben).
             If no clear winner, return None.
    """
    if x == 0 or not nums:
        return None
    
    # Sieve of Eratosthenes to find all prime numbers up to 10000
    MAX_N = 10000
    is_prime = [True] * (MAX_N + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(MAX_N ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX_N + 1, i):
                is_prime[j] = False
    
    primes = [i for i in range(2, MAX_N + 1) if is_prime[i]]
    
    def play_game(n):
        """
        Simulate the game for a given n.
        
        Args:
            n (int): The upper limit of numbers in the game.
        
        Returns:
            str: The winner of the game (Maria or Ben).
        """
        if n == 1:
            return "Ben"
        
        primes_in_game = [p for p in primes if p <= n]
        move_count = 0
        
        while primes_in_game:
            prime = primes_in_game.pop(0)
            multiples = list(range(prime, n + 1, prime))
            primes_in_game = [p for p in primes_in_game if p not in multiples]
            move_count += 1
        
        if move_count % 2 == 0:
            return "Ben"
        else:
            return "Maria"
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
