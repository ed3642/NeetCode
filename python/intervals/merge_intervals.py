class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        
        intervals.sort(key=lambda x: x[0]) # sort by start times

        n = len(intervals)
        res = []
        
        i = 0
        while i < n:
            new_start, new_end = intervals[i]
            while i < n and intervals[i][0] <= new_end: # skip overlapping intervals
                new_end = max(intervals[i][1], new_end)
                i += 1
            res.append([new_start, new_end])
        
        return res