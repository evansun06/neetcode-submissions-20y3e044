class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - position[i]) / speed[i] for i in range(len(position))]
        order = sorted(range(len(position)), key=lambda i: position[i], reverse=True)

        stack = []

        for i in order:
            t = time[i]
            if not stack or t > stack[-1]:
                stack.append(t)

        return len(stack)