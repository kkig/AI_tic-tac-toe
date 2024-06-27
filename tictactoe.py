"""
Tic Tac Toe Player
"""

import math
import copy
from util import *

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Validate input
    if len(board) == 0 or len(board[0]) == 0:
        raise ValueError("Invalid board state")

    total_cells, filled_cells = 0, 0

    # Count cells
    for row in board:
        total_cells += len(row)

        filled_cells += row.count(X)
        filled_cells += row.count(O)

    # All cells are already filled
    if filled_cells == total_cells:
        return None
    
    # Player is X or initial start
    if filled_cells%2 == 0:
        return X
    
    # Player is O
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Validate input
    if len(board) == 0 or len(board[0]) == 0:
        raise ValueError("Invalid board state")
    
    # Get all possible actions (i, j)
    result = set()
    board = copy.deepcopy(board)
    for i, row in enumerate(board):
        while EMPTY in row:
            j = row.index(EMPTY)
            result.add((i, j))
            row[j] = "X"

    # No action was available
    if len(result) == 0:
        return None
    
    # Return pairs
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Validate input
    if len(board) == 0 or len(board[0]) == 0:
        raise ValueError("Invalid board state")
    
    x, y = action

    if board[x][y] != EMPTY:
        raise ValueError("Invalid action")
    
    board = copy.deepcopy(board)
    board[x][y] = player(board)

    return board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in enumerate(board):
        # Holizontal match
        if result := hol_match(row):
            return result   

    if result := ver_match(board):
        return result  
    
    if result := diagnal_match(board):
        return result
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
