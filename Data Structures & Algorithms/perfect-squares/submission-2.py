import math
from functools import cache

class Solution:
    def numSquares(self, n: int) -> int:

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for target in range(1, n + 1):
            for i in range(1, int(math.sqrt(target)) + 1):
                square = i * i

                dp[target] = min(
                    dp[target],
                    1 + dp[target - square]
                )

        return dp[n]