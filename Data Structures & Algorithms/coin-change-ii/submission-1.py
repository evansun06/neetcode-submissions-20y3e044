class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        [1,2,3] make 4

        -1- 1
            -1- 2
                -1- 3
                    -1- 4 sol
                    -2- 5 x
                    -3- 6 x
                -2- 4 sol
                -3- 5 x
            -2- 3
                -1- 4
                -2- 5 x
            -3- 4 sol

        -2- 2

        -3- 3

        state[amount][coin]
        """

        memo = [[None]*len(coins) for _ in range(amount)]

        def dfs(total, i):
            if total > amount:
                return 0
            if total == amount:
                return 1
            
            if memo[total][i] is not None:
                return memo[total][i]
            
            unique_ways = 0
            for j in range(i, len(coins)):
                unique_ways += dfs(total + coins[j], j)

            memo[total][i] = unique_ways
            return unique_ways
        
        return dfs(0,0)
        
                
