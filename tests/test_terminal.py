from tictactoe import *

def test_values():
    assert terminal([[None, None, None], 
                    [None, None, None], 
                    [None, None, None]]) == False
    assert terminal([["X", "O", "O"], 
                    ["O", "X", "X"], 
                    ["X",  "X", "O"]]) == True
    assert terminal([["X", "O", "O"], 
                    ["O", "X", "O"], 
                    ["X",  "X", "X"]]) == True