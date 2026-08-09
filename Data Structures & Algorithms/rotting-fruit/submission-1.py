from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh_oranges = 0

        queue = deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                elif grid[row][col] == 2:
                    # enqueue rotton oranges
                    queue.append((row, col))
        
        time = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue and fresh_oranges > 0:
            print(queue)
            time += 1
            
            for _ in range(len(queue)):

                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (
                        0 <= new_row < len(grid)
                        and 0 <= new_col < len(grid[0])
                        and grid[new_row][new_col] == 1
                    ): 
                        fresh_oranges -= 1
                        grid[new_row][new_col] = 2
                        queue.append((new_row, new_col))
                

            
            
        
        return time if fresh_oranges == 0 else -1
                
                


