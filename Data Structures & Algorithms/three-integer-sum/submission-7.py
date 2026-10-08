class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-1, 0, 1, 2, -1, 4]

        [-1, -1, 0, 1, 2, 4]

        """
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            target = - nums[i]

            # traditional 2sum
            l, r = i + 1, len(nums) - 1

            while l < r:

                while l < r and l > i + 1 and nums[l] == nums[l-1]:
                    l += 1
                while l < r and r < len(nums) - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                    
                if l == r:
                    break
                    
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                elif total > target:
                    r -= 1
                elif total < target:
                    l += 1

        return res