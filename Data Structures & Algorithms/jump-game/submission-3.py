class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Dynamic programming solution
        """

        memo = [None] * len(nums)

        def dfs(i):
            if i >= len(nums) - 1:
                return True
            if memo[i] is not None:
                return memo[i]
            if nums[i] == 0:
                memo[i] = False
                return False
        
            for nxt in range(1, nums[i] + 1):
                if dfs(i + nxt):
                    memo[i] = True
                    return True
            memo[i] = False
            return False

        return dfs(0)
