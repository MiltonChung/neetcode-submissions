"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort the intervals
        intervals.sort(key=lambda i: i.start)

        for i in range(len(intervals)):
            if i + 1 < len(intervals) and intervals[i].end > intervals[i+1].start:
                return False
        
        return True