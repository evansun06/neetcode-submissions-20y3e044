class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        let (i, j) -> int represent the number of unique paths to the end

        recurse and memoize dfs

        base case:
        - memo is not None -> return memo
        - col, row = end -> return 1
        - out of bounds -> return 0
        """

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        memo = [[None] * cols for _ in range(rows)]

        def dfs(r, c):
            
            if r >= rows or c >= cols:
                return 0
            
            if obstacleGrid[r][c] == 1:
                return 0

            if r == rows - 1 and c == cols - 1:
                return 1


            if memo[r][c] is not None:
                return memo[r][c]

            res =  dfs(r + 1, c) + dfs(r, c + 1)
            memo[r][c] = res
            return res
        
        return dfs(0,0)
