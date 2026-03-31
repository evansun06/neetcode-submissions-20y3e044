class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums_sorted = sorted(set(nums))
        max_count = 1
        count = 1
        for i in range(1, len(nums_sorted)):
            prev = nums_sorted[i-1]
            if nums_sorted[i] - prev == 1:
                count+=1      
            else:
                if count > max_count:
                    max_count = count
                count = 1
            prev = nums_sorted[i]
            
        if count > max_count:
                    max_count = count
        return max_count