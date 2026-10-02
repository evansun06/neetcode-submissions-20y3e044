class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Buy low sell high
        Iterate through the array, maintaining the max profit
        if a lower buy is found, buy then.
        """

        max_profit = 0
        buy = 0

        for day, price in enumerate(prices):

            if price < prices[buy]:
                buy = day
            
            max_profit = max(max_profit, price - prices[buy])
        
        return max_profit