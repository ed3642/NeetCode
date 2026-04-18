# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair
import heapq
from typing import List

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        
        LEAVE = 0
        ENTER = 1
        events = []

        for i, (ti, tf) in enumerate(times):
            events.append((ti, ENTER, i))
            events.append((tf, LEAVE, i))

        events.sort(key=lambda x: (x[0], x[1]))
        
        last_seat = 0
        earliest_seat = [] # min heap
        seats = {}
        for _, type, i in events:
            if type == ENTER:
                assigned_seat = -1
                if earliest_seat:
                    assigned_seat = heapq.heappop(earliest_seat)
                else:
                    assigned_seat = last_seat
                    last_seat += 1
                if i == targetFriend:
                    return assigned_seat
                seats[i] = assigned_seat
            elif type == LEAVE:
                heapq.heappush(earliest_seat, seats[i])
        
        return -1