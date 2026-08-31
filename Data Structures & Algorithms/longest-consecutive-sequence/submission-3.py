class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                j = 1
                while num + j in nums:
                    j += 1
                
                longest = max(longest, j)

        return longest

        