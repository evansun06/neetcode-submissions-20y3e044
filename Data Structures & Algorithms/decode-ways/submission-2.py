from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        1234
            A 234 
                B 34
                    C 4
                        D 
                    
                W 4
                    D  
            L 34
                C 4
                    D

        L 23
        """
        @cache
        def dfs(substring:str) -> int:
            # return the # number of unique ways to decode substring
            if len(substring) == 0:
                return 1

            if substring[0] == "0":
                return 0
            
            ways = dfs(substring[1:])
            
            if len(substring) >= 2:
                if 10 <= int(substring[0:2]) <= 26:
                    ways += dfs(substring[2:])

            return ways
        return dfs(s)

        

        

        