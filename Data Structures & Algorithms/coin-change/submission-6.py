class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        [1, 10, 25], 30

        """

        memo = [None] * amount

        def dfs(value: int) -> int:

            if value > amount:
                return float('inf')
            if value == amount:
                return 0
            
            if memo[value] is not None:
                return memo[value]

            min_coins = float('inf')
            for coin in coins:
                min_coins = min(
                    min_coins,
                    dfs(value + coin)
                )

            memo[value] = min_coins + 1
            return memo[value]
        
        min_coins = dfs(0)
        return min_coins if min_coins != float('inf') else -1

                