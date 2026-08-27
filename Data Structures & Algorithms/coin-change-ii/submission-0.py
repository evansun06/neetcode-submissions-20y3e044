class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """

        1 
        -> 1, 1
            -> 1, 1, 1
                    -> 1, 1, 1, 1  +
                    -> 1, 1, 1, 2  x
                    -> 1, 1, 1, 3, x
            -> 1, 1, 2 +
            -> 1, 1, 3 x
        -> 1, 2
            -> 1, 2, 2 x
            -> 1, 2, 3 x
        -> 1, 3 +

        2
        -> 2, 2 +
        -> 2, 3 x

        """

        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for sub_amount in range(coin, amount + 1):
                dp[sub_amount] += dp[sub_amount - coin]

        return dp[amount]
        
                

            

