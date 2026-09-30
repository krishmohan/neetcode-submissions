"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()

        i = 0
        j = 0
        n = len(intervals)
        count = 0
        ans = 0

        while i < n and j < n:
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            ans = max(count, ans)
        
        return ans