class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_max = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            prev_max = max(prev_max + nums[i], nums[i])

            if prev_max > res:
                res = prev_max

        return res

