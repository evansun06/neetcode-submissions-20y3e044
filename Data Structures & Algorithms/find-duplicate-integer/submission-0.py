class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sort = sorted(nums)
        for i in range(1, len(nums)):
            if sort[i] == sort[i-1]:
                return sort[i]