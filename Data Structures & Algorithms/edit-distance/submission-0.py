class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
            let (i, j) -> int represent the number of operations
            required to create word2[:j + 1] after processing word[: i + 1]
        """
        
        len1 = len(word1)
        len2 = len(word2)
        memo = [[None] * len2 for _ in range(len1)]

        def dfs(i, j):

            if i == len1:
                return len2 - j
            
            if j == len2:
                return len1 - i
            
            if memo[i][j] is not None:
                return memo[i][j]
            
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                result = min(
                    dfs(i, j + 1),      # insert
                    dfs(i + 1, j),      # delete
                    dfs(i + 1, j + 1)   # replace
                ) + 1

                memo[i][j] = result
                return result
        
        return dfs(0,0)
