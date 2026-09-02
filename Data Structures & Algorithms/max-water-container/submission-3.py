class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best_area = float('-inf')
        left_max = 0
        right_max = len(heights) - 1
        left = 0
        right = len(heights) - 1

        while left < right:
            best_area = max(best_area, (right_max - left_max) * min(heights[left_max], heights[right_max]))

            if heights[left_max] <= heights[right_max]:
                left += 1
                left_max = left if heights[left_max] < heights[left] else left_max
            else:
                right -= 1
                right_max = right if heights[right_max] < heights[right] else right_max
        
        return best_area
            

