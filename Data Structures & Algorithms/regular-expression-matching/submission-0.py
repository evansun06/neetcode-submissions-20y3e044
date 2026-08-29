class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        """
            state = (i = index of s, j = index of p)
            strip all ".*" from p

            s = "aa" p = ".b"

            choices:
                - letter (raw check)
                - letter*
                    - skip letter
                    - 
                - . 
                - .*

        """

        memo = [[None] * (len(p) + 1) for _ in range(len(s) + 1)]

        def dfs(i, j):
        
            if j == len(p):
                return i == len(s)

            if memo[i][j] is not None:
                return memo[i][j]

        
            first_match = (
                i < len(s)
                and (s[i] == p[j] or p[j] == ".")
            )

            if (
                j + 1 < len(p) and p[j + 1] == "*"
            ):
                res = (
                    dfs(i, j + 2)
                    or
                    first_match and dfs(i + 1, j)
                )
            else:
                res = first_match and dfs(i + 1, j + 1)

            memo[i][j] = res
            return res
        
        return dfs(0, 0)

    