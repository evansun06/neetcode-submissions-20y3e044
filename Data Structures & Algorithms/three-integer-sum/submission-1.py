from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            sort the array nums
            for each element x in nums
            - we try to find a pair of elements that sum to -x
            - skip duplicates
        """

        nums.sort()
        result = []

        for x in range(len(nums)):

            if x > 0 and nums[x] == nums[x - 1]:
                continue

            left, right = x + 1, len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + nums[x]
                
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    result.append([nums[x], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -=1
        

        return result
                
