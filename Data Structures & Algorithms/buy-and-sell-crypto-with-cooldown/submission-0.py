class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        dp = [0] * n

        for sell in range(1, n):
            dp[sell] = dp[sell - 1]

            for buy in range(sell):
                prev_profit = dp[buy - 2] if buy >= 2 else 0

                dp[sell] = max(
                    dp[sell],
                    prev_profit + prices[sell] - prices[buy]
                )

        return dp[-1]