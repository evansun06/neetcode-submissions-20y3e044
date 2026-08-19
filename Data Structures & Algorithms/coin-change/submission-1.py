from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(amount):
            if amount == 0:
                return 0

            min_count = float('inf')
            for coin in coins:

                if coin <= amount:
                    min_count = min(
                        min_count,
                        1 + dfs(amount - coin)
                    )
            
            return min_count
        
        res = dfs(amount)
        return res if res != float('inf') else -1

        