class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l_i = 0
        r_i = len(heights) - 1
        l_h = heights[l_i]
        r_h = heights[r_i]
        width = r_i - l_i
        maxArea = width * min(l_h, r_h)
        while l_i < r_i:
            l_h = heights[l_i]
            r_h = heights[r_i]
            width = r_i - l_i
            area = width * min(l_h, r_h)
            if area >= maxArea:
                maxArea = area
            if l_h > r_h:
                r_i -= 1
            else:
                l_i += 1
            
        return maxArea