class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower:int = 0
        upper:int = len(nums) - 1

        while lower <= upper:
            mid = (upper + lower) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                upper = mid - 1
            else:
                lower = mid + 1
        
        return -1

