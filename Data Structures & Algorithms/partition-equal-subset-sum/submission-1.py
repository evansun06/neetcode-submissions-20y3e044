

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        subsets bruteforce O(2^n) dfs
        """
        
        
        
        total = sum(nums)

        if total % 2 == 1:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for s in range(target, num - 1, -1):
                dp[s] = dp[s] or dp[s - num]
        
        return dp[target]
            

        """
            [1, 2, 3, 5]
            num = 2
            s =  3
            target = 5
            [True, True, True, True, False, False]
            
        """
