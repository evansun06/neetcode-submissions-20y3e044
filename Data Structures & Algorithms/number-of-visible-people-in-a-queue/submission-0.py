class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        result = [0] * len(heights)
        stack = []

        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]

            while stack and stack[-1] < height:
                stack.pop()
                result[i] += 1

            if stack:
                result[i] += 1

                # Current person blocks this equal-height person
                # from the perspective of anyone farther left.
                if stack[-1] == height:
                    stack.pop()

            stack.append(height)

        return result