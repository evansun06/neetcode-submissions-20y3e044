class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        unique_subsets = []

        def backtrack(path, i):
            
            if path not in unique_subsets:
                unique_subsets.append(path.copy())

            if i >= len(nums):
                return

            path.append(nums[i])
            backtrack(path, i+1)
            path.pop()
            backtrack(path, i+1)

        backtrack([], 0)
        return list(unique_subsets)
