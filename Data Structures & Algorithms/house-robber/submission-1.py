from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # at each index i we choose to rob or not rob a house
        # if we rob we got to i + 2 house 
        # if we don't rob we go next door

        @cache
        def _rob(house: int):

            if house >= len(nums):
                return 0
            
            return max(_rob(house + 1), nums[house] + _rob(house + 2))
        
        return _rob(0)
