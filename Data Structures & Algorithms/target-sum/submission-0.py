from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        """
                state = (i = index, sum = )
                        2                     -2
                2+2            2-2      -2+2            -2-2
            2+2+2   2+2-2   2-2+2

        """

        memo = {}

        def dfs(i, val):
            if i == len(nums):   
                return 1 if val == 0 else 0

            if (i, val) in memo:
                return memo[(i, val)]
            

            res = dfs(i + 1, val + nums[i]) + dfs(i + 1, val - nums[i])
            memo[(i, val)] = res
            return res
        
        return dfs(0, target)
            





        
        