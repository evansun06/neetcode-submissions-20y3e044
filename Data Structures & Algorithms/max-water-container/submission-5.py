class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        max_area = float('-inf')

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(area, max_area)
            if heights[left] >= heights[right]:
                right -= 1
            else:
                left += 1
        
        return max_area