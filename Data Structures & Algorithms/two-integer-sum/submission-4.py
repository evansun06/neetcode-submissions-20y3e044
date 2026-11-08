class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for j in range(len(nums)):
            candidate = target - nums[j]
            if candidate in index_map:
                return [index_map[candidate], j]
            index_map[nums[j]] = j