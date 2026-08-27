class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        result = []
        path = []

        def dfs(n, path_sum):
            if path_sum == target:
                result.append(path.copy())

            for i in range(n, len(nums)):
                if path_sum + nums[i] <= target:

                    path.append(nums[i])
                    dfs(i, path_sum + nums[i])
                    path.pop()
        
        dfs(0, 0)
        return result

