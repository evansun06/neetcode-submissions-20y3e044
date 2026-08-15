from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache
        def minCost(i, payed):
    
            if i >= len(cost):
                return payed 

            return min(minCost(i + 1, payed + cost[i]), minCost(i + 2, payed + cost[i]))
        
        return min(minCost(0, 0), minCost(1, 0))
