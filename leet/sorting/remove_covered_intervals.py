# https://leetcode.com/problems/remove-covered-intervals

from typing import List

class Solution:

    # O(n log n)
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        N = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        eater_i = 0 # see how many this one can eat
        removed = 0

        for i in range(1, N):
            c, d = intervals[eater_i]
            a, b = intervals[i]
            if c <= a and b <= d:
                removed += 1
            else:
                eater_i = i
        
        return N-removed

    # O(n^2)
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        N = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        removed = 0
        isremoved = [False] * N

        for i in range(N):
            c, d = intervals[i]
            for j in range(i+1, N):
                if isremoved[j]:
                    continue
                a, b = intervals[j]
                if c <= a and b <= d:
                    removed += 1
                    isremoved[j] = True
        
        return N-removed