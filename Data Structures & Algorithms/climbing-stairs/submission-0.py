from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def ways(i):
            if i == n:
                return 1

            if i > n:
                return 0

            return ways(i + 1) + ways(i + 2)
        
        return ways(0)