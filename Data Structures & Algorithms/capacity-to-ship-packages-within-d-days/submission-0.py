class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        we are searching for a minimum weight capacity such that
        we can ship within d <=`days`

        Binary search

        0 < max capacity per day <= sum(weights)

        [1,2,3,4,5] days = 5

        (0, 16]
        mid = 8, days = 3

        left value mid such that sim_day <= days
        """

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (left + right) // 2

            sim_days = 1
            load = 0

            for weight in weights:
                if load + weight > mid:
                    sim_days += 1
                    load = 0
                load += weight

            if sim_days > days:
                left = mid + 1
            else:
                right = mid
        
        return left
    