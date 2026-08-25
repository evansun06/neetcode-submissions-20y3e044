class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        possible moves: down, right
        state: row, col -> unique ways to get there

        top down: memoization (m, n)
            uniquePaths(m, n) == 1
            uniquePaths(row, col) = sum(uniquePaths(row + 1, col), uniquePaths(row, col + 1))
        """

        memo = [[None] * n for _ in range(m)]

        directions = [(0, 1), (1, 0)]

        def dfs(row, col):

            if row == m - 1 and col == n - 1:
                return 1
            
            if memo[row][col] is not None:
                return memo[row][col]
            
            paths = 0

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < m and 0 <= new_col < n:
                    paths += dfs(new_row, new_col)
                

            memo[row][col] = paths
            return paths

        return dfs(0, 0)

        



