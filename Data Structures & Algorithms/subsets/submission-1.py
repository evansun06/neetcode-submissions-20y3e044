class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        unique_subsets = []

        def backtrack(path, i):

            if i == len(nums):
                unique_subsets.append(path.copy())
                return

            path.append(nums[i])
            backtrack(path, i+1)

            path.pop()
            backtrack(path, i+1)

        backtrack([], 0)
        return unique_subsets
