import pytest
from tictactoe import player

def test_empty():
    with pytest.raises(ValueError):
        player([[]])

def test_init():
    assert player([[None, None, None], 
                   [None, None, None], 
                   [None, None, None]]) == "X"