class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[None] * cols for _ in range(rows)]

        def dfs(row, col):
            if row >= rows or col >= cols:
                return 0  

            if memo[row][col] is not None:
                return memo[row][col]
            
            if matrix[row][col] == "0":
                memo[row][col] = 0
                return 0
            else:
                result = 1 + min(
                    dfs(row + 1, col),
                    dfs(row, col + 1),
                    dfs(row + 1, col + 1)
                )

                memo[row][col] = result
                return result
        
        best = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == "1":
                    best = max(dfs(row, col), best)

        return best*best

                

        