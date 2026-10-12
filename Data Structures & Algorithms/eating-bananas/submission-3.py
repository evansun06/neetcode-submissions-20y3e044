class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Binary Search
        k in (0, max(piiles)]

        for each mid we will simulate hours
        
        if sim_hours > h
            left = mid + 1
        elif sim_hours <= h:
            right = mid

        """

        left, right = 1, max(piles)

        while left < right:

            # k candidate
            mid = (left + right) // 2

            sim_hours = 0
            for pile in piles:
                sim_hours += (pile + mid - 1) // mid
            
            if sim_hours > h:
                left = mid + 1
            else:
                right = mid

        return left


            