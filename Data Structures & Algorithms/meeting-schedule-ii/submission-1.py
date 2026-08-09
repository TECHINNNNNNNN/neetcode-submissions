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
        count = 0
        for i in intervals:
            start.append(i.start)
            end.append(i.end)
        
        start.sort()
        end.sort()

        s = 0
        e = 0
        max_room = 0

        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                count += 1
                max_room = max(max_room,count)
                s += 1
            else:
                count -= 1
                e += 1
        
        return max_room

        