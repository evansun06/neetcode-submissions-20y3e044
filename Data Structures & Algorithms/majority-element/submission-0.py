from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = defaultdict(int)
        majority = len(nums) / 2
        for num in nums:
            counter[num] += 1;

            if counter[num] > majority:
                return num

        