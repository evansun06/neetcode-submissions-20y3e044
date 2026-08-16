class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0 
        flipped_zeros = 0
        max_ones = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                flipped_zeros += 1
        
            while flipped_zeros > k:
                if nums[left] == 0:
                    flipped_zeros -= 1
                
                left += 1
            
            max_ones = max(max_ones, right - left + 1)
        
        return max_ones

            

