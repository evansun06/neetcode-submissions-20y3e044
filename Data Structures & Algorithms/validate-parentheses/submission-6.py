class Solution:
    def isValid(self, s: str) -> bool:
        """
        Stack?

        "({})[]"

        One pass iteration, maintaining a stack of left brackets
        Pop when iteration is onright bracket
        Return false if stack[-1] != right bracket
        Otherwise True
        """

        stack = []
        bracket_map = {"[": "]", "{":"}", "(":")"}

        for bracket in s:
            
            if bracket in bracket_map:
                stack.append(bracket)
            elif not stack or bracket_map[stack.pop()] != bracket:
                return False
        
        return not stack

        
