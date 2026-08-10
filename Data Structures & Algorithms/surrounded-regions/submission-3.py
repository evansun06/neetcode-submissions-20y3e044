from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()

        def bfs(coord):
            directions = [
                (0, 1),
                (1, 0),
                (0, -1),
                (-1, 0)
            ]

            q = deque([coord])
            visited.add(coord)

            region = {coord}
            surrounded = True

            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    # Check bounds FIRST
                    if not (
                        0 <= new_row < len(board)
                        and 0 <= new_col < len(board[0])
                    ):
                        continue

                    if (
                        board[new_row][new_col] == "X"
                        or (new_row, new_col) in visited
                    ):
                        continue

                    visited.add((new_row, new_col))
                    region.add((new_row, new_col))
                    q.append((new_row, new_col))

                    # This O touches the border
                    if (
                        new_row == 0
                        or new_row == len(board) - 1
                        or new_col == 0
                        or new_col == len(board[0]) - 1
                    ):
                        surrounded = False

            if surrounded:
                for row, col in region:
                    board[row][col] = "X"

        for row in range(1, len(board) - 1):
            for col in range(1, len(board[0]) - 1):
                if board[row][col] == "O" and (row, col) not in visited:
                    bfs((row, col))