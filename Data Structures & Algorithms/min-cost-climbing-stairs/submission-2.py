from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        @cache
        def minCost(i):
            if i >= len(cost):
                return 0

            return cost[i] + min(
                minCost(i + 1),
                minCost(i + 2)
            )

        return min(minCost(0), minCost(1))