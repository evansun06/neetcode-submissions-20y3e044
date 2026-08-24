class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = [None] * len(nums)

        def dfs(n:int) -> tuple(int, int):
            # return min val of the sequence and length of increasing sequence

            if memo[n] is not None:
                return memo[n]
            
            best = 1

            for i in range(n+1, len(nums)):
                if nums[i] > nums[n]:
                    best = max(best, 1 + dfs(i))
            
            memo[n] = best
            return memo[n]

        
        result = max(dfs(i) for i in range(len(nums)))

        return result

        """
        [4, 10, 4, 3, 8, 9]
        memo = [3, 1, 3, 3, 2, 1]

        
        """


            
  