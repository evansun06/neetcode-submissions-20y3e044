class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0

        for day, price in enumerate(prices):
            if price < prices[buy]:
                buy = day
            
            max_profit = max(max_profit, price - prices[buy])

        return max_profit
