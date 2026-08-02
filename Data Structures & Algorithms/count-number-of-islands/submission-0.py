class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
                    
        def isNewIsland(row, col) -> bool:
            # dfs approach
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return False

            if (row, col) in visited:
                return False
            
            visited.add((row,col))

            if grid[row][col] == "0":
                return False
            else:
                isNewIsland(row + 1, col)
                isNewIsland(row - 1, col)
                isNewIsland(row, col + 1)
                isNewIsland(row, col - 1)
                return True
                
        for row in range(len(grid)):
            for col in range(len(grid[0])):

                if isNewIsland(row, col):
                    islands += 1

        return islands

                    
        