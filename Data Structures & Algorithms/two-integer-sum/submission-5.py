class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indice_map = {}

        for i, num in enumerate(nums):
            candidate = target - num

            if candidate in indice_map:
                return [indice_map[candidate], i]
            
            indice_map[num] = i