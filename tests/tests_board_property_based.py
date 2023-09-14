import pytest

from life.logic.board import Board

property_based_test_params = [
    (' | | | \n'\
     ' | | | \n'\
     ' | | | \n'\
     ' | | | '),
    (' | | | \n'\
     ' | | | '),
    (' | \n' \
     ' | '),
    (' | | | \n'\
     ' | | | \n'\
     ' | | | \n'\
     ' | | | \n'\
     ' | | | \n'\
     ' | | | '),
    (' |o\n' \
     'o| '),
    (' |o| |o\n' \
     ' | | | \n' \
     ' |o| | \n' \
     ' | | | \n' \
     ' | |o| \n' \
     ' | | | ')
]


@pytest.mark.parametrize("board_str", property_based_test_params)
def test_2x4_board_from_string(board_str):
    board = Board.from_string(board_str)
    assert board.__str__() == board_str