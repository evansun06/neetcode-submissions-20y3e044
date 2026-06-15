class Solution:
    def findMin(self, nums: List[int]) -> int:
        # invariants of a unique + rotated + sorted array:
        # the element left of nums[i] is less
        # the element right of nums[i] is greater
        left = 0
        right = len(nums) - 1

        while right >= left:
            mid = (left + right) // 2

            if (nums[mid] > nums[(mid + 1) % len(nums)]):
                return nums[(mid + 1) % len(nums)]
            elif  (nums[(mid - 1) % len(nums)] > nums[mid]):
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
        return nums[mid]


