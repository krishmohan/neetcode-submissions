"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        starts = []
        ends = []

        for iv in intervals:
            starts.append(iv.start)
            ends.append(iv.end)
        
        starts.sort()
        ends.sort()

        i = 0
        j = 0
        count = 0
        res = 0

        while i < n and j < n:
            if starts[i] < ends[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(count, res)

        return res