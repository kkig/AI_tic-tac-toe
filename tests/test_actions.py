from tictactoe import actions

def test_values():
    assert actions([["X", None, "X"], 
                    ["X", "X", "X"], 
                    ["X", None, "X"]]) == {(0, 1), (2, 1)}
    
    assert actions([[None, None, "X"], 
                    ["X", "O", None], 
                    ["O", None, "X"]]) == {(0, 0), (0, 1), (1, 2), (2, 1)}