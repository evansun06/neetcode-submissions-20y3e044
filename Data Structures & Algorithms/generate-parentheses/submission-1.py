class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = set()

        def backtrack(i: int, combo: str):
            if i == n:
                result.add(combo)
                return
            
            # left
            backtrack(i + 1, "()" + combo)
            # right
            backtrack(i + 1, combo + "()")
            for p in range(len(combo)):
                if combo[p] == "(":
                    backtrack(i + 1, combo[:p + 1] + "()" + combo[p + 1:])

        backtrack(1, "()")

        return list(result)