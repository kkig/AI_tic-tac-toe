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
    board: A list of lists containg values, representing board.
    Assume input will be valid.

    Returns player who has the next turn on a board.
    """
    total_cells, filled_cells = 0, 0

    # Count cells
    for row in board:
        total_cells += len(row)
        filled_cells += sum(1 for x in row if x != EMPTY)

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
    board: A list of lists containg values, representing board.
    Assume input will be valid.

    Returns set of all possible actions (i, j) available on the board.
    """    
    # Get all possible actions (i, j)
    result = set()
    board = copy.deepcopy(board)
    for i, row in enumerate(board):
        while EMPTY in row:
            j = row.index(EMPTY)
            result.add((i, j))
            row[j] = X

    # No action was available
    if len(result) == 0:
        return None
    
    # Return pairs
    return result


def result(board, action):
    """
    board: A list of lists containg values, representing board.
    Assume input will be valid.
    action: Tuple, (i, j) coordinate on the board to fill.

    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if board[i][j] != EMPTY:
        raise ValueError("Invalid action")
    
    board = copy.deepcopy(board)
    board[i][j] = player(board)

    return board


def winner(board):
    """
    board: A list of lists containg values, representing board.
    Assume input will be valid.

    Returns the winner of the game, if there is one.
    """
    # Diagnal match
    if result := diagnal_match(board):
        return result
    
    # Horizontal match
    for row in board:
        if result := hol_match(row):
            return result
        
    if result := ver_match(board):
        return result
    
    return None


def terminal(board):
    """
    board: A list of lists containg values, representing board.
    Assume input will be valid.

    Returns True if game is over, False otherwise.
    """
    # No more available space
    if is_empty(board):
        return True
    
    # Horizontal match
    if winner(board):
        return True
    
    return False


def utility(board):
    """    
    board: A list of lists containg values, representing board.
    Assume input will be valid.

    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.

    Assume to be called when terminal(board) is True.
    """
    if result := winner(board):
        return 1 if result == X else -1
    
    return 0


def minimax(board):
    """
    board: A list of lists containg values, representing board.
    Assume input will be valid.

    Returns the optimal action for the current player on the board.
    Return None when board is terminal.
    """
    raise NotImplementedError
