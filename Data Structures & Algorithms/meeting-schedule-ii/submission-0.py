"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #  [(0,40),(5,10),(15,20)]
        # min_heap = []
        # min_heap = [40]
        # 40 <= 5 -> False
        # min_heap = [10, 40]
        # 10 <= 15 -> True
        # min_heap = [20, 40]
        intervals.sort(key=lambda interval: interval.start)

        min_heap = []
        max_rooms = 0

        for interval in intervals:
            while min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval.end)
            max_rooms = max(max_rooms, len(min_heap))

        return max_rooms


