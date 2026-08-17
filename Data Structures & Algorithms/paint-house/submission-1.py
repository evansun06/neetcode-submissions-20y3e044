from functools import cache

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        
        @cache
        def dfs(n, prev_color) -> int:
            if n == len(costs):
                return 0
            
            if prev_color == None:
                return min(
                    costs[n][0] + dfs(n+1, 0),
                    costs[n][1] + dfs(n+1, 1),
                    costs[n][2] + dfs(n+1, 2)
                )
            elif prev_color == 1:
                return min(
                    costs[n][0] + dfs(n+1, 0),
                    costs[n][2] + dfs(n+1, 2)
                )
            elif prev_color == 2:
                return min(
                    costs[n][0] + dfs(n+1, 0),
                    costs[n][1] + dfs(n+1, 1)
                )
            else:
                return min(
                    costs[n][1] + dfs(n+1, 1),
                    costs[n][2] + dfs(n+1, 2)
                )

        return dfs(0, None)

        