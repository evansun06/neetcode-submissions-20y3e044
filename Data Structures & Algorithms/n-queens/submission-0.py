class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        queens = []

        used_cols = set()
        used_diagonal_1 = set()  # row - col
        used_diagonal_2 = set()  # row + col

        def backtrack(row):
            # Successfully placed one queen in every row
            if row == n:
                result.append(map_sol(queens))
                return

            # Try every column in the current row
            for col in range(n):
                diagonal_1 = row - col
                diagonal_2 = row + col

                if (
                    col in used_cols
                    or diagonal_1 in used_diagonal_1
                    or diagonal_2 in used_diagonal_2
                ):
                    continue

                # Choose
                queens.append((row, col))
                used_cols.add(col)
                used_diagonal_1.add(diagonal_1)
                used_diagonal_2.add(diagonal_2)

                # Explore the next row
                backtrack(row + 1)

                # Undo
                queens.pop()
                used_cols.remove(col)
                used_diagonal_1.remove(diagonal_1)
                used_diagonal_2.remove(diagonal_2)

        def map_sol(queens):
            board = [["."] * n for _ in range(n)]

            for row, col in queens:
                board[row][col] = "Q"

            return ["".join(row) for row in board]

        backtrack(0)
        return result