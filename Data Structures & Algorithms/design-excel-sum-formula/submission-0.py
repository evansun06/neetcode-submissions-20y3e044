from collections import defaultdict
from typing import List


class Cell:
    def __init__(self):
        self.value = 0

        # Cells this cell depends on.
        # dependency -> multiplicity
        self.dependencies = defaultdict(int)

        # Formula cells that depend on this cell.
        self.dependents = set()


class Excel:

    def __init__(self, height: int, width: str):
        self.height = height
        self.width = ord(width) - ord('A') + 1

        self.sheet = [
            [Cell() for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def _parse_column(self, column: str) -> int:
        return ord(column) - ord('A')

    def _get_cell(self, row: int, column: str) -> Cell:
        return self.sheet[row - 1][self._parse_column(column)]

    def _clear_formula(self, cell: Cell) -> None:
        """
        Remove this cell's old formula.

        If A1 used to depend on B1 and C1, remove A1 from
        B1.dependents and C1.dependents.
        """

        for dependency in cell.dependencies:
            dependency.dependents.remove(cell)

        cell.dependencies.clear()

    def _propagate(self, cell: Cell, delta: int) -> None:
        """
        cell changed by delta.

        Tell every formula that depends on it.
        """

        for dependent in cell.dependents:

            # dependent may reference cell multiple times
            count = dependent.dependencies[cell]

            dependent_delta = delta * count
            dependent.value += dependent_delta

            self._propagate(dependent, dependent_delta)

    def set(self, row: int, column: str, val: int) -> None:
        cell = self._get_cell(row, column)

        # Setting a literal value destroys the old formula.
        self._clear_formula(cell)

        old_value = cell.value
        cell.value = val

        delta = val - old_value

        if delta != 0:
            self._propagate(cell, delta)

    def get(self, row: int, column: str) -> int:
        return self._get_cell(row, column).value

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        cell = self._get_cell(row, column)

        # New formula replaces any old formula.
        self._clear_formula(cell)

        old_value = cell.value
        new_value = 0

        for expression in numbers:

            # Single cell, e.g. "A1"
            if ":" not in expression:
                source = self._parse_reference(expression)

                cell.dependencies[source] += 1
                source.dependents.add(cell)

                new_value += source.value

            # Range, e.g. "A1:C3"
            else:
                start, end = expression.split(":")

                start_row, start_col = self._parse_position(start)
                end_row, end_col = self._parse_position(end)

                for r in range(start_row, end_row + 1):
                    for c in range(start_col, end_col + 1):
                        source = self.sheet[r - 1][c]

                        cell.dependencies[source] += 1
                        source.dependents.add(cell)

                        new_value += source.value

        cell.value = new_value

        delta = new_value - old_value

        if delta != 0:
            self._propagate(cell, delta)

        return cell.value

    def _parse_reference(self, reference: str) -> Cell:
        row, col = self._parse_position(reference)
        return self.sheet[row - 1][col]

    def _parse_position(self, reference: str):
        """
        "B12" -> (12, 1)
        """

        col_char = reference[0]
        row = int(reference[1:])
        col = self._parse_column(col_char)

        return row, col