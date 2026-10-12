class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Array of positive integers:
        - Increasing the window (incr r) increases the window sum
        - Decreasing the window (incr l) decreases the window sum
        best = 3

        [2,1,5,1,5,3] target = 10
        sum = 6
        l = 2, r = 4
        """

        left = 0
        window_sum = 0
        best_len = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                best_len = min(best_len, right - left + 1)
                window_sum -= nums[left]
                left += 1
            
        
        return best_len if best_len != float('inf') else 0