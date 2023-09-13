import pytest

from life.logic.cell import Cell, LiveCell, DeadCell


def test_create_dead_cell_from_str():
    res = Cell.from_string(' ')
    assert res.__eq__(DeadCell())


def test_create_live_cell_from_str():
    res = Cell.from_string('o')
    assert res.__eq__(LiveCell())

# Test negativo
def test_create_cell_error():
    with pytest.raises(ValueError):
        res = Cell.from_string('-')

