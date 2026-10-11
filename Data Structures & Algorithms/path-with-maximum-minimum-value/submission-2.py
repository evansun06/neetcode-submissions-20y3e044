class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        """
        [5,4,5]
        [1,2,6]
        [7,4,6]

        memo state = (row,col), min so far
        """

        best_so_far = [[None] * len(grid[0]) for _ in range(len(grid))]

        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]

        def dfs(row, col, minSoFar):
            
            minSoFar = min(minSoFar, grid[row][col])
            best_so_far[row][col] = minSoFar

            for dr, dc in directions:

                new_row, new_col = row + dr, col + dc

                if (0 <= new_row < len(grid)
                    and 0 <= new_col < len(grid[0])
                ):
                    if (best_so_far[new_row][new_col] is None 
                        or best_so_far[new_row][new_col] < minSoFar
                    ):
                        dfs(new_row,new_col,minSoFar)  
            

        dfs(0,0,grid[0][0])
        return best_so_far[-1][-1]
            
            
