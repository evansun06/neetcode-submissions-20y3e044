class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
            Top Down Approach
        """

        memo = [[None] * len(text2) for _ in range(len(text1))]

        def dfs(i: int, j: int):

            if i < 0 or j < 0:
                return 0
            
            if memo[i][j] is not None:
                return memo[i][j]
            
            if text1[i] == text2[j]:
                memo[i][j] = dfs(i - 1, j - 1) + 1
            else:
                memo[i][j] = max(dfs(i - 1, j), dfs(i, j - 1))
            
            return memo[i][j]
        

        return dfs(len(text1) - 1, len(text2) - 1)
            
        