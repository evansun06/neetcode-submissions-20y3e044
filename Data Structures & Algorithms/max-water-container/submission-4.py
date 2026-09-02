class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best_area = float('-inf')
        left = 0
        right = len(heights) - 1

        while left < right:
            best_area = max(best_area, (right - left) * min(heights[right], heights[left]))

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return best_area
            

