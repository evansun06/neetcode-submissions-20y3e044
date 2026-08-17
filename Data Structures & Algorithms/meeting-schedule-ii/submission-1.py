"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from collections import defaultdict

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        # start_map: time: count
        
        # end_map: time: count

        # min_start and max_end

        # concurrent_meetings = 0

        if len(intervals) == 0:
            return 0

        start_map = defaultdict(int)
        end_map = defaultdict(int)

        min_start = float('inf')
        max_end = float('-inf')

        for i in intervals:

            start_map[i.start] += 1
            end_map[i.end] += 1
            min_start = min(min_start, i.start)
            max_end = max(max_end, i.end)
        

        concurrent_meetings = 0
        max_concurrent_meetings = 0

        for t in range(min_start, max_end + 1):
            max_concurrent_meetings = max(concurrent_meetings, max_concurrent_meetings)

            concurrent_meetings += start_map[t]
            concurrent_meetings -= end_map[t]

        return max_concurrent_meetings
        # [0  8]
        #    [8   10]
        #  [2     10]


