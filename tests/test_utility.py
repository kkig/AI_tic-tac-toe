from tictactoe import *

def test_utility():
    assert utility([["X", "X", "X"], 
                    ["O", "X", "O"], 
                    ["X", None, "O"]]) == 1
    assert utility([["X", "X", "O"], 
                    ["O", "O", "O"], 
                    ["O", None, "X"]]) == -1
    assert utility([["X", "X", "O"], 
                    ["O", "X", "O"], 
                    ["O", None, "X"]]) == 1
    assert utility([["O", "X", "O"], 
                    ["X", "O", "X"], 
                    ["O", None, "O"]]) == -1

    assert utility([["X", "X", "O"], 
                    ["O", "X", "X"], 
                    ["X", "O", "O"]]) == 0 