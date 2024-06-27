def hol_match(row):
    """
    Check holizontal match.
    Returns winner of the match, if there is one.
    """
    p = row[0]
    if row.count(p) == len(row):
        return p
    return None


def ver_match(board):
    """
    Check vertical match.
    Returns winner of the match, if there is one.
    """
    # Horizontal ptr
    for i, elem in enumerate(board[0]):
        if elem == None:
            continue
        
        # Vertical ptr
        for j in range(1, len(board)):
            if board[j][i] != elem:
                break        
        else:
            return elem
    return None


def diagnal_match(board):
    """
    Check diagnal match.
    Return: winner of the match or None
    """
    max_i_index = len(board[0]) - 1
    
    lt = board[0][0]
    if lt != None:
        i = 0
        res = [lt]
        for j in range(1, len(board)):
            i += 1
            res.append(board[j][i])
            if board[j][i] != lt:
                break

        if res.count(lt) == 3:
            return lt

        
    rt = board[0][max_i_index]
    if rt != None:
        i = max_i_index
        res = [rt]
        for j in range(1, len(board)):
            i -= 1
            res.append(board[j][i])
            if board[j][i] != rt:
                break

        if res.count(rt) == 3:
            return rt

    return None
    

