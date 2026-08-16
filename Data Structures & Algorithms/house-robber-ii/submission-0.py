from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        @cache
        def rob_A(n:int):
            # rob the first house
            if n >= len(nums) - 1:
                return 0
            else:
                return max(nums[n] + rob_A(n + 2), rob_A(n + 1))
        @cache
        def rob_B(n:int):
            # don't rob the first house
            if n == len(nums) - 1:
                return nums[n]
            elif n >= len(nums):
                return 0
            else:
                return max(nums[n] + rob_B(n + 2), rob_B(n + 1))

        return max(rob_A(0), rob_B(1))
        