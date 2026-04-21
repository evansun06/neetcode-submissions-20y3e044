class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []   # unresolved indices
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                popped = stack.pop()
                result[popped] = i - popped
            stack.append(i)

        return result