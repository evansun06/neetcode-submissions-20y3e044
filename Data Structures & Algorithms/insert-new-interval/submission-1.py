class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        start_new, end_new = newInterval

        # Find insertion position
        left, right = 0, len(intervals)

        while left < right:
            mid = (left + right) // 2

            if intervals[mid][0] < start_new:
                left = mid + 1
            else:
                right = mid

        intervals.insert(left, newInterval)

        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
                
        return res
