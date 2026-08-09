from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(
        self, heights: List[List[int]]
    ) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        def bfs(start_row, start_col, ocean):
            queue = deque([(start_row, start_col)])
            visited = {(start_row, start_col)}

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if not (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                    ):
                        continue

                    if (new_row, new_col) in visited:
                        continue

                    if ocean == "pacific":
                        is_ocean_edge = (
                            new_row == 0 or new_col == 0
                        )
                    else:
                        is_ocean_edge = (
                            new_row == rows - 1
                            or new_col == cols - 1
                        )

                    if (
                        is_ocean_edge
                        or heights[new_row][new_col]
                        >= heights[row][col]
                    ):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

            return visited

        pacific = bfs(0, 0, "pacific")
        atlantic = bfs(rows - 1, cols - 1, "atlantic")

        both = pacific & atlantic

        return [[row, col] for row, col in both]