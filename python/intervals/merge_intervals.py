# https://leetcode.com/problems/merge-intervals

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        res = []
        N = len(intervals)
        start_t = intervals[0][0]
        end_t = intervals[0][1]

        for i in range(1, N):
            start = intervals[i][0]
            end = intervals[i][1]
            if start > end_t:
                res.append([start_t, end_t])
                start_t = intervals[i][0]
            if intervals[i][1] > end_t:
                end_t = end

        res.append([start_t, end_t])
        return res
    
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