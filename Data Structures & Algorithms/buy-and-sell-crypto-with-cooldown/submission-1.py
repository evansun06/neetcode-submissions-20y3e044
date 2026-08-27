class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n <= 1:
            return 0

        dp = [0] * n

        # best value of dp[buy - 2] - prices[buy]
        best_buy = -prices[0]

        for sell in range(1, n):
            # Either don't sell today,
            # or sell today using the best valid previous buy
            dp[sell] = max(
                dp[sell - 1],
                prices[sell] + best_buy
            )

            # Treat `sell` as a possible buy day for a FUTURE sale.
            # If we buy today, previous transaction must end <= sell - 2.
            prev_profit = dp[sell - 2] if sell >= 2 else 0

            best_buy = max(
                best_buy,
                prev_profit - prices[sell]
            )

        return dp[-1]