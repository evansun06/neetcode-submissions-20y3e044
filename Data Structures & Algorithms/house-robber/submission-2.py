class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        [1,1,3,3]

        memo state = the maximum amount of money we cant rob from i to n
        """

        memo = [None] * len(nums)

        def dfs(i) -> int:
            if i >= len(nums):
                return 0 
            
            if memo[i] is not None:
                return memo[i]

            res = max(nums[i] + dfs(i + 2), dfs(i+ 1))

            memo[i] = res
            return res
        
        return dfs(0)