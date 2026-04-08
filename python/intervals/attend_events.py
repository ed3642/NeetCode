# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended

import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        
        events.sort()
        count = 0
        last_day = max([times[1] for times in events])
        i = 0
        n = len(events)
        heap = []

        for day in range(1, last_day + 1):
            # events that already passed
            while i < n and day > events[i][1]:
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            # consider all events that have started
            while i < n and day >= events[i][0]:
                heapq.heappush(heap, events[i][1])
                i += 1
            # use this event that has started but not ended yet
            # this will also be the event that will end the soonest
            if heap:
                heapq.heappop(heap)
                count += 1

        return count
