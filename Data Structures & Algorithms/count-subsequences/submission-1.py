class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        Backtracking style. Memoize (i, j) which are indices to s and t respectively
        
        Subproblem: How many distince subsequences can be made with s[i:] and t[j:]?
        """

        if len(t) > len(s):
            return 0

        memo = [[None] * len(t) for _ in range(len(s))]

        def dfs(i, j):

            if i >= len(s) or j >= len(t):
                return 0

            if memo[i][j] is not None:
                return memo[i][j]
            
            if s[i] == t[j]:
                if j == len(t) - 1:
                    return 1

                distinct = 0
                for nxt in range(i + 1, len(s)):
                    distinct += dfs(nxt, j + 1)
                
                memo[i][j] = distinct
                return distinct

            else:
                return 0

        result = 0
        for i in range(len(s)):
            result += dfs(i, 0)
        
        return result
        