class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bottom - Up Approach: 
        [0,1,2,3,4,1,n,n,n,n,n,n,n]
        """

        dp = [None] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] is not None:
                    if dp[i] is not None:
                        dp[i] = min(dp[i], dp[i - coin] + 1)
                    else:
                        dp[i] = dp[i - coin] + 1
        
        return dp[amount] if dp[amount] is not None else -1
                

        
