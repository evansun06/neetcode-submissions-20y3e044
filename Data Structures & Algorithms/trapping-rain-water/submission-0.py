class Solution:
    def trap(self, height: List[int]) -> int:
        # water can only be traped in bins with a width of at least 1.
        # there can be no bar between the two edge bars that is taller then them.
        # the height of water trapped is:
        # 1 the minimum between two pillars * width - all the bars in between

        stack = []
        total_water = 0

        for i, current_height in enumerate(height):
            while stack and height[stack[-1]] < current_height:
                bottom_index = stack.pop()

                # No left boundary
                if not stack:
                    break

                left_index = stack[-1]

                width = i - left_index - 1

                bounded_height = (
                    min(height[left_index], current_height)
                    - height[bottom_index]
                )

                total_water += width * bounded_height

            stack.append(i)


            

        return total_water
                

    

            
            
