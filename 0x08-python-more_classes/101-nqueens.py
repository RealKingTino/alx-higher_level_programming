#!/usr/bin/python3
"""Solves the N-queens puzzle. """


import sys

def solve_nqueens(N):
    """
    Solve the N Queens problem and return a list of solutions.
    Each solution is represented as a list of queen positions.
    """
    solutions = []  # Store the solutions
    queens = []  # Store the positions of the queens
    place_queen(0, queens, N, solutions)
    return solutions

def place_queen(row, queens, N, solutions):
    """
    Recursive function to place queens on the chessboard.
    Backtracking is used to find all valid solutions.
    """
    if row == N:
        # All queens have been successfully placed
        solutions.append(list(queens))
        return

    for col in range(N):
        if is_valid(row, col, queens):
            # Place a queen at position (row, col)
            queens.append(col)
            place_queen(row + 1, queens, N, solutions)
            # Backtrack by removing the last queen and trying other positions
            queens.pop()

def is_valid(row, col, queens):
    """
    Check if placing a queen at position (row, col) is valid.
    Return True if there are no conflicts, False otherwise.
    """
    for r, c in enumerate(queens):
        # Check if the current queen conflicts with any previously placed queens
        if c == col or r + c == row + col or r - c == row - col:
            return False
    return True

def print_solutions(solutions):
    """
    Print the solutions in the required format.
    """
    for solution in solutions:
        chessboard = []
        for row in range(len(solution)):
            chessboard.append([row, solution[row]])
        print(chessboard)

if __name__ == "__main__":
    # Validate the input arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem and print the solutions
    solutions = solve_nqueens(N)
    print_solutions(solutions)
