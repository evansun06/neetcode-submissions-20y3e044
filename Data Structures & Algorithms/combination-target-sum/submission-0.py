class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        solution = []

        def backtrack(path: list, sum: int, start: int):
            if sum == target:
                solution.append(path.copy())

            if sum > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
  
                backtrack(path, sum + nums[i], i)

                path.pop()

        
        backtrack([], 0, 0)
        return solution
