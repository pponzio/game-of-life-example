import pytest

from life.logic.board import Board
from life.logic.cell import DeadCell, LiveCell


#@pytest.fixture(scope='module')
@pytest.fixture
def board():
    return Board(2, 2)


def test_initial_board(board):
    assert board.rows == 2
    assert board.columns == 2
    assert board.get_cell(0, 0).__eq__(DeadCell())
    assert board.get_cell(0, 1).__eq__(DeadCell())
    assert board.get_cell(1, 0).__eq__(DeadCell())
    assert board.get_cell(1, 1).__eq__(DeadCell())


def test_put_one_live_cell(board):
    board.put_live_cell(1, 0)
    assert board.get_cell(0, 0).__eq__(DeadCell())
    assert board.get_cell(0, 1).__eq__(DeadCell())
    assert board.get_cell(1, 0).__eq__(LiveCell())
    assert board.get_cell(1, 1).__eq__(DeadCell())


def test_put_live_cell_fails(board):
    board.put_live_cell(1, 0)
    with pytest.raises(ValueError):
        board.put_live_cell(1, 0)


def test_board_to_string(board):
    res = board.__str__()
    expected = ' | \n' \
               ' | '
    assert expected == res
    expected2 = ''' | \n
                    | '''
    assert expected2 == res
