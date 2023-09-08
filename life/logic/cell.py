#Cell
#  - to string
#  - from string

from abc import ABC, abstractmethod


class Cell:

    @staticmethod
    def from_string(cell_str):
        if cell_str == DeadCell().__str__():
            return DeadCell()
        elif cell_str == LiveCell().__str__():
            return LiveCell()
        else:
            raise ValueError(f'Invalid cell string: {cell_str}')

    def __str__(self):
        raise NotImplementedError



class DeadCell(Cell):

    def __str__(self):
        return ' '

    def __eq__(self, other):
        return isinstance(other, DeadCell)


class LiveCell(Cell):

    def __str__(self):
        return 'o'

    def __eq__(self, other):
        return isinstance(other, LiveCell)