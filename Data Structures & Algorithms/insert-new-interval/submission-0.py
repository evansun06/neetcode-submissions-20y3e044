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

        # Merge with previous interval if necessary
        if left - 1 >= 0 and intervals[left - 1][1] >= intervals[left][0]:
            intervals[left][0] = intervals[left - 1][0]
            intervals[left][1] = max(
                intervals[left][1],
                intervals[left - 1][1]
            )

            del intervals[left - 1]
            left -= 1

        # Merge all overlapping intervals to the right
        while (
            left + 1 < len(intervals)
            and intervals[left + 1][0] <= intervals[left][1]
        ):
            intervals[left][1] = max(
                intervals[left][1],
                intervals[left + 1][1]
            )

            del intervals[left + 1]

        return intervals