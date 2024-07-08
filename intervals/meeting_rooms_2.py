"""
Definition of Interval:
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        
        # determine the max num of meetings that are happening at any given timestamp
        times = []

        for interval in intervals:
            times.append((interval.start, True)) # true means its the start of a meeting
            times.append((interval.end, False)) # false means its the end of a meeting
        
        times.sort()
        concurrent_meetings = 0
        rooms_needed = 0
        for _, is_meeting_start in times:
            if is_meeting_start:
                concurrent_meetings += 1
            else:
                concurrent_meetings -= 1
            rooms_needed = max(concurrent_meetings, rooms_needed)

        return rooms_needed