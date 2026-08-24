from collections import defaultdict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = [None] * len(s)
        wordDict = set(wordDict)

        def dfs(n: int):

            if n == len(s):
                return True

            if memo[n] is not None:
                return memo[n]

            res = False

            for i in range(n + 1, len(s) + 1):
                candidate = s[n:i]
                if candidate in wordDict and dfs(i):
                    memo[n] = True
                    return True
                
            memo[n] = res

            return res

        return dfs(0)

    """
    n:0

    [None, None, None, None, None, None, None, None]

    """
            
            


        