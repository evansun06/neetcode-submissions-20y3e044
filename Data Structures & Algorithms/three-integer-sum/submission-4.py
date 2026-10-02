class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort the Array to help with duplicates

        Brute force solution O(n^3): triple loop comparing all possible triplets
        - skip duplicates if nums[i] == nums[i - 1]

        Two Sum can be solve on O(n): hashmap or two pointer

        ThreeSum can be solved in O(n^2) if we just do twoSum n times.
        """

        n = len(nums)
        nums.sort()
        result = []

        for i, num in enumerate(nums):

            # check duplicates
            if i > 0 and num == nums[i - 1]:
                continue
                
            target = -num

            left, right = i + 1, n - 1

            while left < right:
                while left < right and left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                
                while left < right and right < n - 1 and nums[right] == nums[right + 1]:
                    right -= 1

                if left == right:
                    break
                
                total = nums[left] + nums[right]

                if total == target:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return result
        