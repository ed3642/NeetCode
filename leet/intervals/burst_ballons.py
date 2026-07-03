# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        n = len(points)
        points.sort(key=lambda x: x[0])

        darts = 0

        i = 0
        while i < n:
            _, r2 = points[i]

            i += 1
            while i < n and points[i][0] <= r2:
                r2 = min(points[i][1], r2)
                i += 1
            
            darts += 1

        return darts
    
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        
        if len(points) == 1:
            return 1

        intervals = sorted(points, key=lambda x: x[1])
        last_end = intervals[0][1]
        need = 1

        for start, end in intervals[1:]:
            if start > last_end:
                need += 1
                last_end = end

        return need