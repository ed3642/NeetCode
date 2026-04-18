# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        
        OPEN = 0
        CLOSE = 1
        events = []

        for ti, tf in intervals:
            events.append((ti, OPEN))
            events.append((tf, CLOSE))
        
        events.sort()

        concurrent = 0
        max_concurrent = 0
        for _, type in events:
            if type == OPEN:
                concurrent += 1
            elif type == CLOSE:
                concurrent -= 1
            max_concurrent = max(concurrent, max_concurrent)
        
        return max_concurrent