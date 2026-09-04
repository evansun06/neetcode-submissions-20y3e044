class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        """
        brute force might be running dfs on each element in the matrix.

        is there a subproblem?

        """
        rows = len(matrix)
        cols = len(matrix[0])
        memo = [[None] * cols for _ in range(rows)]

        directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1)
        ]

        def dfs(row, col):

            if memo[row][col] is not None:
                return memo[row][col]

            
            best = 1

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and matrix[row][col] < matrix[new_row][new_col]
                ):
                    best = max(best, dfs(new_row, new_col) + 1)
            
            memo[row][col] = best

            return best
        
        longest_pos_path = 1

        for i in range(rows):
            for j in range(cols):
                longest_pos_path = max(longest_pos_path, dfs(i, j))
        
        return longest_pos_path

            
            