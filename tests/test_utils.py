from util import *

def test_is_match():
    # Black box test
    assert is_match([]) == False
    assert is_match(["X"]) == False
    assert is_match(["X", "Y"]) == False

    # Glass box test
    assert is_match(["X", "X"]) == True
    assert is_match(["Y", "Y", "Y"]) == True


def test_hol_match():
    assert hol_match(["X", "X", "X"]) == "X"
    assert hol_match(["O", "O", "O"]) == "O"    
    assert hol_match([None, None, None]) == None
    assert hol_match(["O", None, "X"]) == None


def test_ver_match():
    assert ver_match([["O", None, "X"], 
                    ["X", "O", "O"], 
                    ["X", None, "X"]]) == None
    assert ver_match([["X", None, "X"], 
                    ["X", "O", "O"], 
                    ["X", None, "X"]]) == "X" 
    assert ver_match([["X", "X", "O"], 
                    ["O", "X", "O"], 
                    ["X", None, "O"]]) == "O"
    
def test_diagnal():
    assert diagnal_match([["X", "X", "X"], 
                        ["O", "X", "O"], 
                        ["X", None, "O"]]) == "X"
    assert diagnal_match([["X", "X", "O"], 
                        ["O", "O", "O"], 
                        ["O", None, "X"]]) == "O"
    assert diagnal_match([["X", "X", "O"], 
                        ["O", "X", "O"], 
                        ["O", None, "X"]]) == "X"
    assert diagnal_match([["O", "X", "O"], 
                        ["X", "O", "X"], 
                        ["O", None, "O"]]) == "O"
    
    assert diagnal_match([["O", "X", "O"],
                        ["X", None, "X"], 
                        ["O", None, "O"]]) == None
    assert diagnal_match([[None, "X", "O"],
                        ["O", "X", "X"], 
                        ["O", None, "O"]]) == None
    assert diagnal_match([["X", "X", None],
                        ["O", "X", "X"], 
                        ["O", None, "O"]]) == None    