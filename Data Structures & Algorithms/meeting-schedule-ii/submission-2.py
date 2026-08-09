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

        count = 0
        i = 0
        j = 0

        print(f"start {start}")
        print(f"end {end}")

        while i < len(start) and j < len(end):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                i += 1
                j += 1
            print(f"count {count} i:{i} j:{j}")


        return count
        


        