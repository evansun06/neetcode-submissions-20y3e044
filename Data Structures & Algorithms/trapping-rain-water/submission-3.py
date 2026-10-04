class Solution:
    def trap(self, height: List[int]) -> int:
        """
        [2, 0, 3]

        """
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0

        total_rainwater = 0

        while left <= right:
            if rightMax >= leftMax:
                if height[left] <= leftMax:
                    total_rainwater +=  (leftMax - height[left])
                
                leftMax = max(height[left], leftMax)
                left += 1
            else:
                if height[right] <= rightMax:
                    total_rainwater +=  (rightMax - height[right])

                rightMax = max(height[right], rightMax)
                right -= 1
                

        return total_rainwater
                
