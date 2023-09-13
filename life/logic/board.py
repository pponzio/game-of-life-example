#Board:
#  - rows
#  - columns
#  - to string
#  - create from string
#  - put live cell
from life.logic.cell import DeadCell, LiveCell


class Board:

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


    def __str__(self):
        rows_str = ['|'.join(row) for row in self.board]
        return '\n'.join(rows_str)
    