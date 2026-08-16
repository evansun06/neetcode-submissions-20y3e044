class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        mid = x
        while left <= right:
            mid = (left + right) // 2

            square = mid * mid
            if square == x:
                return mid
            elif square > x:
                right = mid - 1
            else:
                left = mid + 1
    
        return right
