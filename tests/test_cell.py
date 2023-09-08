from life.logic.cell import Cell, LiveCell


def test_create_live_cell_from_str():
    res = Cell.from_string(' ')
    assert isinstance(res, LiveCell)
