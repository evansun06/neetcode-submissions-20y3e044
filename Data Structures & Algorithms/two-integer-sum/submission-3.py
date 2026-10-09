class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [3,4,5,6] target = 9
        i = 2
        {3:0, 4: 1}
        9 -5 = 4
        """

        index_map = {}

        for i, num in enumerate(nums):
            if target - num in index_map:
                return [index_map[target-num], i]
            index_map[num] = i