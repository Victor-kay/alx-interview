#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve_nqueens(board, row, n, solutions):
    if row == n:
        solutions.append(list(board))
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, n, solutions)

def print_solutions(solutions):
    for solution in solutions:
        print([[i, col] for i, col in enumerate(solution)])

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solutions = []
    solve_nqueens(board, 0, n, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
