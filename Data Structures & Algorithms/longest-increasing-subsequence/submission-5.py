class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        
        """
        memo = {}

        def dfs(i, prev):
            if i == len(nums):
                return 0
            
            if (i, prev) in memo:
                return memo[(i, prev)]
            
            # skip
            skip = dfs(i + 1, prev)

            # consume
            consume = 0

            if prev is None or nums[i] > prev:
                consume = 1 + dfs(i + 1, nums[i])


            memo[(i, prev)] = max(consume, skip, 0)
            return memo[(i, prev)]
        
        return dfs(0, None)
