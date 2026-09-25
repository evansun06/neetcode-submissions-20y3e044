from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi-breath first search
        
        First pass O(m*n):
        - count the # of fresh fruit
        - and collect the # of rotten fruit

        Then Multi-Breadth First Search O(m*n*4)
        """

        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        fresh_fruit = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_fruit += 1
                elif grid[row][col] == 2:
                    q.append((row, col))
                    visited.add((row, col))
        
        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        minutes = 1
        
        while q:
            for _ in range(len(q)):

                row, col = q.popleft()

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    coord = (new_row, new_col)

                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and coord not in visited
                        and grid[new_row][new_col] == 1
                    ):
                        fresh_fruit -= 1
                        if fresh_fruit == 0:
                            return minutes
                        q.append(coord)
                        visited.add(coord)

            minutes += 1
        
        return -1 if fresh_fruit != 0 else 0

