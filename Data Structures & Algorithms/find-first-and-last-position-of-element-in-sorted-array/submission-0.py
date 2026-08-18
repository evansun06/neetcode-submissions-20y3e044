class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
    

        def binarySearch(nums, target):

            left, right = 0, len(nums) - 1

            mid = (right + left) // 2

            while right >= left:
                mid = (right + left) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1
        
        search = binarySearch(nums, target)

        if search == -1:
            return [-1, -1]
        else:
            # fan out
            left, right = search, search

            while right < len(nums):
                if right + 1 < len(nums) and nums[right + 1] == target:
                    right += 1
                else: 
                    break

            while left > 0:
                if left - 1 >= 0 and nums[left - 1] == target:
                    left -= 1
                else: 
                    break
            return [left, right]

