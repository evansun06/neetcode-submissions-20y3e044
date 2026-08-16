"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
from collections import defaultdict

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        schedules = [interval for employee_schedule in schedule for interval in employee_schedule]
        schedules.sort(key = lambda interval: interval.start)

        overlapping = []

        for interval in schedules:
            if not overlapping:
                overlapping.append(interval)
            
            if interval.start <= overlapping[-1].end:
                overlapping[-1].end = max(overlapping[-1].end, interval.end)
            else:
                overlapping.append(interval)
        
        result = []
        for i in range(1, len(overlapping)):
            free_interval = Interval(overlapping[i-1].end, overlapping[i].start)
            result.append(free_interval)

        return result