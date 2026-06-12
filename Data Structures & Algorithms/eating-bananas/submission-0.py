class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k <= max(piles)
        # t = x/k
        # t = 
        right = max(piles)
        left = 1
        mid = right
        while right >= left:
            mid = (right + left) // 2
            
            hours = 0
            for bananas in piles:
                hours += (bananas + mid - 1) // mid
            
            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1
                
        return left