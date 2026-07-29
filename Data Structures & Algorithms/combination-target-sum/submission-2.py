class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        path = []
        result = []

        def backtrack(sum: int, i: int):
            if len(nums) == i or sum > target:
                return
            
            if sum == target:
                result.append(path.copy())
                return
            

            path.append(nums[i])
            backtrack(sum + nums[i], i)
            path.pop()
            
            backtrack(sum, i + 1)
    
        backtrack(0, 0)

        return result