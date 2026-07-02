class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(nlogn) brute force solution
        for i in range(len(nums)):
            if nums[abs(nums[i])] < 0:
                return abs(nums[i])
            else:
                nums[abs(nums[i])] *= -1
            
