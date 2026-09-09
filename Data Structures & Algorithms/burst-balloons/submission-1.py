class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """

            [1] + [4,2,3] + [1]


        choose which balloon to pop last
        - recurse this decision
        """

        nums = [1] + nums + [1]

        n = len(nums)  # After padding
        memo = [[None] * n for _ in range(n)]

        def dfs(left, right):

            if left + 1 == right:
                return 0
            
            if memo[left][right] is not None:
                return memo[left][right]
            
            max_value = 0

            for k in range(left + 1, right):

                max_value = max(
                    max_value,
                    (dfs(left, k) + dfs(k, right) + (nums[left] * nums[k] * nums[right]))
                )

            memo[left][right] = max_value
            
            return max_value

        return dfs(0, len(nums) - 1)
        