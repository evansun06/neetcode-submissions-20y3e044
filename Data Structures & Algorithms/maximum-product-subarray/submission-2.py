
class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min = nums[0]

        result = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            cur_max = max(
                x,
                x * prev_max,
                x * prev_min
            )

            cur_min = min(
                x,
                x * prev_max,
                x * prev_min
            )

            result = max(result, cur_max)

            prev_max = cur_max
            prev_min = cur_min

        return result


        