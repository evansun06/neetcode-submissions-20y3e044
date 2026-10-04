class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = [None] * len(nums)

        def dfs(i) -> int:
            if i >= len(nums) - 1:
                return 0
            if memo[i] is not None:
                return memo[i]
            
            best = float('inf')
            for j in range(1, nums[i] + 1):
                best = min(dfs(i + j), best)
            
            memo[i] = best + 1
            return best + 1
        
        return dfs(0)
                
