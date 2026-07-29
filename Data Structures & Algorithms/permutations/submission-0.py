class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        marker = [False] * len(nums)
        result = []

        def backtrack(i: int, path: list[int]):
            if i == len(nums):
                result.append(path.copy())
            
            for x in range(0, len(nums)):
                if not marker[x]:
                    marker[x] = True
                    path.append(nums[x])
                    backtrack(i + 1, path)
                    marker[x] = False
                    path.pop()
        
        backtrack(0, [])

        return result