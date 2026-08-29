class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[None] * len(matrix[0]) for _ in range(len(matrix))]

        def dfs(row, col):

            if row >= rows or col >= cols:
                return 0
            
            if memo[row][col] is not None:
                return memo[row][col]
            
            if matrix[row][col] == "1":
                memo[row][col] =  1 + min(
                    dfs(row + 1, col),
                    dfs(row + 1, col + 1),
                    dfs(row, col + 1)
                )
                return memo[row][col]
            else:
                return 0

        max_side = 0

        for row in range(rows):
            for col in range(cols):
                max_side = max(max_side, dfs(row, col))
        
        return max_side*max_side
            
            
                
            

            



        