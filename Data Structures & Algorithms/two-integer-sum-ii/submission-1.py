class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = left + (right - left)//2
                x = target - numbers[i]
                if x == numbers[mid]:
                    return [i + 1, mid + 1]
                elif x < numbers[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return []