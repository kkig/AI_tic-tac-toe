def hol_match(row):
    """
    row: List, a row of the board 
    Check holizontal match.

    Return: Winner of the match, or None.
    """
    if all(row[0] == col for col in row[1:]):
        return row[0]
    
    return None


def ver_match(board):
    """
    board: List of row lists
    Check vertical match.

    Return: Winner of the match, or None.
    """
    row0, _, _ = board
    
    # Horizontal ptr
    for i, col in enumerate(row0):
        cells = [board[1][i], board[2][i]]
        if all(cell == col for cell in cells):
            return col
    #     cell_val = board[0][i]
    #     evals = [cell_val == board[j][i] for j in range(1, len(board))]

    #     if False not in evals:
    #         return cell_val  
    return None


def diagnal_match(board):
    """
    board: List of row lists, assuming 3 x 2 board.

    Return: Winner of the match, or None
    """
    # Center is empty
    if not board[1][1]:
        return None
    
    # Diagnal match, left top
    lt_group = [board[1][1], board[2][2]]

    if all(col == board[0][0] for col in lt_group):
        return board[0][0]
    
    
    # Diagnal match, right top
    rt_group = [board[1][1], board[2][0]]
    
    if all(col == board[0][2] for col in rt_group):
        return board[0][2]

    return None


def is_match(group):
    """
    group: List, should be more than 1 elements in it.

    return: Boolean, whether all elements are the same or not.
    """
    # No elements to evaluates
    if len(group) <= 1 or None in group:
        return False

    if all(x == group[0] for x in group[1:]):
        return True
    
    return False

    
    
def is_empty(board):
    for row in board:
        if None in row:
            return False
            
    return True


print(is_match(["X", "Y"]))