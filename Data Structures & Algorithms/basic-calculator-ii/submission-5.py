class Solution:
    def calculate(self, s: str) -> int:

        """
         3+2*2

         operations = [+]
         stack = [3, 4]
        """
        s = s.replace(" ", "")
        
        stack = []
        sumOps = []
        ops = set(["+", "/", "*", "-"])
        i = 0
        
        while i < len(s):
            token = s[i]
            if token in ops:
                
                if token == "+" or token == "-":
                    sumOps.append(token)
                    i += 1
                else:
                    first = stack.pop()

                    j = i + 1
                    while j < len(s) and s[j] not in ops:
                        j += 1
                    
                    second = int(s[i + 1:j])

                    if token == "*":
                        stack.append(first * int(second))
                    else:
                        stack.append(int(first / second))
                    i = j      
            else:
                j = i
                while j < len(s) and s[j] not in ops:
                    j += 1
                token = s[i:j]
                stack.append(int(token))

                i += (j-i)
        
        result = stack[0]
        for i in range(1, len(stack)):
            if sumOps[i - 1] == "+":
                result += stack[i]
            else:
                result -= stack[i]

        return result

                
                    

        