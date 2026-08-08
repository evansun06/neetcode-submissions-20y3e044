class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def inBoundary(coord) -> bool:
            return 0 <= coord[0] < len(grid) and 0 <= coord[1] < len(grid[0])

        def area(coord) -> int:
            # dfs implementation 
            if not inBoundary(coord) or grid[coord[0]][coord[1]] == 0:
                return 0
            else:
                grid[coord[0]][coord[1]] = 0

                a = 1
                a += area((coord[0] + 1, coord[1]))
                a += area((coord[0] - 1, coord[1]))
                a += area((coord[0], coord[1] + 1))
                a += area((coord[0], coord[1] - 1))
                return a
        
        max_area = 0

        for row in range(len(grid)):
            for column in range(len(grid[0])):

                if grid[row][column] == 0:
                    continue
                else:
                    max_area = max(max_area, area((row, column)))
        
        return max_area
                
                

    
        

    
