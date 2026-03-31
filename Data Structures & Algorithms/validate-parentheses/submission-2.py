class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = ["(", "[", "{"]
        for p in s:
            if p in openers:
                stack.append(p)
            else:
                if not stack:
                    return False
                popped = stack.pop()

                if p == ")":
                    if popped != "(":
                        return False
                elif p == "]":
                    if popped != "[":
                        return False 
                else:
                    if popped != "{":
                        return False
        
        return (len(stack) == 0)