class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        # monotomic stack. Store (start, height). Stores the ascending heights
        # where start represents how far a height can extend back.

        stack = []
        greatest_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] >= h:
                start, height = stack.pop()
                greatest_area = max(greatest_area, height*(i-start))
            
            stack.append((start, h))

        
        for start, height in stack:
            width = len(heights) - start
            greatest_area = max(greatest_area, height * width)
        
        return greatest_area



                
                




        
        

        
