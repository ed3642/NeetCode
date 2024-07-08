# https://leetcode.com/problems/insert-interval/description/
class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        res = []
        insert_start, insert_end = newInterval
        n = len(intervals)
        placed = False

        i = 0
        while i < n:
            start, end = intervals[i]
            if end >= insert_start: # intersects
                insert_start = min(start, insert_start)
                while i < n and intervals[i][0] <= insert_end: # skip intersecting intervals
                    insert_end = max(intervals[i][1], insert_end)
                    i += 1
                res.append([insert_start, insert_end]) # append new interval
                placed = True
                while i < n: # append the remaining
                    res.append(intervals[i])
                    i += 1
            else:
                res.append(intervals[i])
            i += 1

        if not placed: # must be at the end
            res.append(newInterval)
        return res