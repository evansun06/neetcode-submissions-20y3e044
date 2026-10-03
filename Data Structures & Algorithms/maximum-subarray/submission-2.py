class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadanes algorithm O(n):negative prefix sums + candidate is worse than the candidate itself

        - Goal: The sum of a contiguous subarray

        Prefix sum = nums[0]
        Iterate through the entire array of nums:
            if prefix sum <= 0:
                prefix sum = nums[i]
            else prefix sum += nums[i]

        """

        prefix_sum = 0
        best = nums[0]
        
        for i in range(len(nums)):
            if prefix_sum < 0:
                prefix_sum = nums[i]
            else:
                prefix_sum += nums[i]
            
            best = max(prefix_sum, best)
    
        return best