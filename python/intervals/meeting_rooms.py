class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])

        last_end = 0
        for interval in intervals:
            if interval[0] < last_end:
                return False
            last_end = interval[1]
        
        return True