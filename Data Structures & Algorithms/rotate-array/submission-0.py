class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        old = nums.copy()

        for i in range(len(nums)):
            nums[i] = old[(i-k)%len(nums)]
        