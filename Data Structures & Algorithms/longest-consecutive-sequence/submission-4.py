class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        make the entire array nums a set:
        
        iterate i, num in enumerate(nums):
        if num - 1 not in set: -> we know this value is a potential start
        j = 1
        while num + j in set:
            j += 1
        
        """

        nums = set(nums)
        longest = 0

        for num in nums:

            if num - 1 not in nums:
                j = 1

                while num + j in nums:
                    j += 1
                
                if j > longest:
                    longest = j
                    
        return longest
                

                