class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)

        dp = [1] * n
        parent = [-1] * n

        best_len = 1
        best_end = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            if dp[i] > best_len:
                best_len = dp[i]
                best_end = i

        result = []

        while best_end != -1:
            result.append(nums[best_end])
            best_end = parent[best_end]

        return result[::-1]