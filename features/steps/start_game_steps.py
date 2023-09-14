from features.environment import table_from_string
from life.logic.game_state import GameState, GameMode


@given(u'the game is not started')
def step_impl(context):
    pass


@when(u'we create a new game with an {rows:d}x{columns:d} board')
def step_impl(context, rows, columns):
    context.state.new_game(rows, columns)

@then(u'the game should be in cells placement mode')
def step_impl(context):
    assert context.state.mode == GameMode.CELLS_PLACEMENT

@then(u'the state of the board should be')
def step_impl(context):
    table_str = table_from_string(context.table)
    assert context.state.board.__str__() == table_str
