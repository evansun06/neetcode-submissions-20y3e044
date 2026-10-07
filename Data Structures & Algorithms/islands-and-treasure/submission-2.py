from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Multi BFS on the treasures chests
        [INF, -1, 0, 1]
        [INF,INF, 1, -1]
        [1  , -1,INF, -1]
        [0  , -1,INF,INF]]

        visited = {(2,0), (0,3), (1, 2)}
        distance = 1
        """

        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        distance = 0

        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0, -1)
        ]
        while q:
            for _ in range(len(q)):

                r, c = q.popleft()
     
                grid[r][c] = distance

                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc

                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and (new_row, new_col) not in visited
                        and grid[new_row][new_col] != -1
                    ):
                        q.append((new_row, new_col))
                        visited.add((new_row, new_col))

            distance += 1
        




