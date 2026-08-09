"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        if not intervals:
            return 0
        
        intervals.sort(key=lambda x : (x.start, x.end))

        endHeap = []

        heapq.heappush(endHeap, intervals[0].end)

        for interval in intervals[1:]:
            if interval.start >= endHeap[0]:
                heapq.heappop(endHeap)
            heapq.heappush(endHeap, interval.end)
        return len(endHeap)
        


        