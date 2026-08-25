class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = [None] * (amount + 1)

        def dfs(value: int):

            if value == 0:
                return 0
            
            if memo[value] is not None:
                return memo[value]
            
            min_coins = float('inf')
            for coin in coins:

                if value - coin >= 0:
                    min_coins = min(
                        min_coins,
                        dfs(value - coin)
                    )

            min_coins += 1
            memo[value] = min_coins
            return min_coins

        result = dfs(amount)
        return result if result != float('inf') else -1
            

