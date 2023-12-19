class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        interval_span = [0, 0]
        new_intervals = []
        l = newInterval[0]
        r = newInterval[1]

        for start, end in intervals:
            if l >= start:
                interval_span[0] = start
            if r <= end:
                interval_span[1] = end
            if l < start and r > end:
                new_intervals.append([start, end])
        
        return new_intervals