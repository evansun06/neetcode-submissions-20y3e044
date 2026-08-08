class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()

        def multi_bfs():

            while q:

                row, col = q.popleft()
                directions = [
                    (1, 0),
                    (-1, 0),
                    (0, 1),
                    (0, -1)
                ]

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (0 <= new_row < len(grid)
                        and 0 <= new_col < len(grid[0])
                        and grid[new_row][new_col] == 2147483647
                    ):
                        grid[new_row][new_col] = grid[row][col] + 1
                        q.append((new_row, new_col))


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    q.append((row, col))

        multi_bfs()
        
        

            

