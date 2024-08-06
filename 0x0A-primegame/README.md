# Prime Game

## Description
This project implements the Prime Game, where two players, Maria and Ben, take turns choosing prime numbers from a set of consecutive integers starting from 1 up to and including `n`. The chosen prime number and its multiples are removed from the set. The player who cannot make a move loses the game. Maria always goes first. Both players play optimally. The program determines the winner of each game for `x` rounds and returns the player with the most wins. If there's no clear winner, it returns `None`.

## Requirements
- Python 3.4.3
- Ubuntu 20.04 LTS

## Usage
The main function is `isWinner(x, nums)`:
- `x` (int): The number of rounds.
- `nums` (list): A list of integers representing the upper limit of numbers for each round.

The function returns the name of the player that won the most rounds. If no player wins more rounds, it returns `None`.

## Example
```python
#!/usr/bin/python3

from 0-prime_game import isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
# Expected Output: Winner: Ben
