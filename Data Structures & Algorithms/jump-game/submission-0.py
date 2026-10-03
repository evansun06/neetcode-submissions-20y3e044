class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Brute force we might try to simulate the jumps from index 0 O(n^2)

        Instead we maintain a capped suffix sum representing the distance we can currently make going backwards. If the value at i + suffix_sum >= len(nums) - i, then suffix_sum = len(nums) - 1. 
        """
        n = len(nums)
        suffix_sum = 0
        for i in range(n - 2, -1, -1):
            if suffix_sum + nums[i] >= (n - 1 - i):
                suffix_sum = n - 1 - i
        
        return suffix_sum == n - 1


