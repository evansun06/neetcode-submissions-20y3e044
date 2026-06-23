class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack indexes?
        stack = [len(temperatures) - 1]
        result = [0] * len(temperatures)

        for i in reversed(range(len(temperatures) - 1)):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i
            
            stack.append(i)

            
        
        return result