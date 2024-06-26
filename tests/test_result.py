from tictactoe import result
import pytest

def test_empty():
    with pytest.raises(ValueError):
        result([[]], (0, 0))

def test_invalid_action():
    with pytest.raises(ValueError):
        result([["X", None, "X"], 
                ["X", "X", "X"], 
                ["X", None, "X"]], (0, 0))
        
def test_value():
    result([["O", None, "X"], 
            ["X", "O", "O"], 
            ["X", None, "X"]], (0, 1)) ==  [["O", "O", "X"], 
                                            ["X", "O", "O"], 
                                            ["X", None, "X"]]

    result([["X", None, "X"], 
            ["X", "O", "O"], 
            [None, None, "O"]], (2, 0)) == [["X", None, "X"], 
                                            ["X", "O", "O"], 
                                            ["X", None, "O"]]