class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        """
        sliding window
        """

        unique = set(nums)
        best_gain = 0


        for value in unique:

            if value == k:
                continue

            prev = 0
            i = 0
            for j in range(len(nums)):
                if prev < 0:
                    prev = 0
                    i = j

                if nums[j] == k:
                    prev -= 1
                elif nums[j] == value:
                    prev += 1

                best_gain = max(best_gain, prev)

        return best_gain + nums.count(k)
            
                
            
            

