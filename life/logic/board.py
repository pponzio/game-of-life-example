#Board:
#  - rows
#  - columns
#  - to string
#  - create from string
#  - put live cell
from life.logic.cell import DeadCell, LiveCell, Cell


class Board:

    @staticmethod
    def from_string(board_str):
        rows = board_str.split('\n')
        n_rows = len(rows)
        if n_rows < 1:
            raise ValueError(f'Invalid number of rows: {n_rows}')
        matrix = [row.split('|') for row in rows]
        n_cols = len(matrix[0])
        if n_cols < 1:
            raise ValueError(f'Invalid number of columns: {n_cols}')
        for row in range(n_rows):
            row_len = len(matrix[row])
            if row_len != n_cols:
                raise ValueError(f'Invalid number of columns: {row_len}')

        return Board._from_string_matrix(n_rows, n_cols, matrix)

    @staticmethod
    def _from_string_matrix(rows, cols, matrix):
        new_board = Board(rows, cols)
        for row in range(rows):
            for col in range(cols):
                curr_cell = matrix[row][col]
                new_board.put_cell(row, col, Cell.from_string(curr_cell))
        return new_board

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.board = []
        for row in range(self.rows):
            curr_row = []
            for col in range(self.columns):
                curr_row.append(DeadCell())
            self.board.append(curr_row)

    def get_cell(self, row, column):
        return self.board[row][column]

    def put_live_cell(self, row, column):
        if self.get_cell(row, column).__eq__(LiveCell()):
            raise ValueError

        self.board[row][column] = LiveCell()

    def put_cell(self, row, column, cell):
        self.board[row][column] = cell

    @staticmethod
    def _row_to_string(row):
        res = ''
        columns = len(row)
        for col in range(columns):
            res += row[col].__str__()
            if col < columns - 1:
                res += '|'
        return res

    def __str__(self):
        res = ''
        for row_num in range(self.rows):
            res += Board._row_to_string(self.board[row_num])
            if row_num < self.rows - 1:
                res += '\n'
        return res
