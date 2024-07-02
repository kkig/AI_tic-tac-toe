from tictactoe import winner

    
def test_winners():
    assert winner([["X", "X", "X"], 
                    ["O", "X", "O"], 
                    ["X", None, "O"]]) == "X"
    assert winner([["O", "X", "O"],
                    ["X", None, "X"], 
                    ["O", None, "O"]]) == None