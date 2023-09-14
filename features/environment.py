from behave import fixture, use_fixture

from life.logic.game_state import GameState


def table_from_string(table):
    rows_list = []
    for row in table.rows:
        curr_row = []
        for elem in row:
            if elem == '':
                curr_row.append(' ')
            elif elem == 'o':
                curr_row.append('o')
            else:
                raise ValueError(f'Unknown cell value: {elem}')
        rows_list.append('|'.join(curr_row))
    return '\n'.join(rows_list)


def close_db_connection():
    pass

@fixture
def state(context):
    #, *args, **kwargs):
    context.state = GameState()
    # crear objeto
    yield context.state
    close_db_connection()
    # limpiar el objeto


def before_feature(context, feature):
    use_fixture(state, context)