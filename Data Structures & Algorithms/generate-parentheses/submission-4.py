class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        n = 1
        ()

        n = 2


        n = 3 
        (())()

        n = 4
        (())(())
        """
        
        res = []
        def dfs(openCount, closedCount, parenth):
            if len(parenth) == 2*n:
                res.append(parenth)
                return
            if openCount < n:
                dfs(openCount + 1, closedCount, parenth + '(')
            if closedCount < openCount:
                dfs(openCount, closedCount + 1, parenth + ')')

        dfs(0,0, "")
        return res
                