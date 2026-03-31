class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, n in enumerate(nums):
            x = target - n
            if x in map:
                return [map[x], i]
            else:
                map[n] = i