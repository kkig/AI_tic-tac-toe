from tictactoe import player

def test_init():
    assert player([[None, None, None], 
                   [None, None, None], 
                   [None, None, None]]) == "X"