# https://leetcode.com/problems/insert-interval

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        n = len(intervals)
        l, r = newInterval
        res = []

        for i, (s, e) in enumerate(intervals):
            # overlaps with this interval
            if s <= l <= e or s <= r <= e or (l <= s and e <= r):
                new_s = min(l, s)
                temp_e = max(e, r)
                while i < n and intervals[i][0] <= temp_e:
                    temp_e = max(intervals[i][1], temp_e)
                    i += 1
                # put in the new interval
                res.append([new_s, temp_e])
                # close
                if i < n:
                    res.extend(intervals[i:])
                return res
            elif i > 0 and intervals[i-1][1] < l and r < s: # nonoverlapping between intervals
                res.append(newInterval)
                # close
                if i < n:
                    res.extend(intervals[i:])
                return res
            else:
                res.append([s, e])

        # didnt find intervals that overlapped, new interval must be at the end or at the start
        if intervals and r < intervals[0][0]:
            res.insert(0, newInterval)
        else:
            res.append(newInterval)

        return res
    
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