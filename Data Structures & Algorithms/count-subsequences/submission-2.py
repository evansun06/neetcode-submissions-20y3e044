class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        """
        Subproblem:
        dfs(i, j) = number of ways to construct t[j:]
                    using characters from s[i:]
        """

        memo = {}

        def dfs(i, j):

            # Successfully constructed all of t
            if j == len(t):
                return 1

            # Ran out of s before constructing t
            if i == len(s):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            # Always allowed to skip s[i]
            distinct = dfs(i + 1, j)

            # Or consume s[i] if it matches t[j]
            if s[i] == t[j]:
                distinct += dfs(i + 1, j + 1)

            memo[(i, j)] = distinct
            return distinct

        return dfs(0, 0)