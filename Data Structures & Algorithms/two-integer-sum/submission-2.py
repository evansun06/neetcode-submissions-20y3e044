class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indice_map = {}
        
        for i in range(len(nums)):
            candidate = target - nums[i]

            if candidate in indice_map:
                return [indice_map[candidate], i]

            indice_map[nums[i]] = i