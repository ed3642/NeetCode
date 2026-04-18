# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii

import bisect
from collections import defaultdict
from typing import List

class Solution:

    # O(n)
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        
        n = len(startTime)
        # stoppers
        startTime.append(eventTime)
        endTime.append(eventTime)
        max_gap_found = startTime[0]
        can_move = [False] * n
        
        max_before = 0
        for i in range(n):
            time = endTime[i] - startTime[i]
            if time <= max_before:
                can_move[i] = True
            max_before = max(startTime[i] - endTime[i - 1] if i > 0 else startTime[i], max_before)
        max_after = 0
        for i in range(n - 1, -1, -1):
            time = endTime[i] - startTime[i]
            if time <= max_after:
                can_move[i] = True
            max_after = max(startTime[i + 1] - endTime[i], max_after)

        before = startTime[0]
        for i in range(n):
            meeting_time = endTime[i] - startTime[i]
            after = startTime[i + 1] - endTime[i]
            if can_move[i]:
                # put it somewhere else
                max_gap_found = max(before + meeting_time + after, max_gap_found)
            else:
                # try to put it in the before or after gap
                max_gap_found = max(before + after, max_gap_found)
            before = startTime[i + 1] - endTime[i]
        
        return max_gap_found

    # O(n log k)
    def maxFreeTime2(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        
        n = len(startTime)
        gaps = []
        # 0 to first event
        gaps.append(startTime[0])
        # stoppers
        startTime.append(eventTime)
        endTime.append(eventTime)
        max_gap = startTime[0]

        for i in range(n):
            gaps.append(startTime[i + 1] - endTime[i])

        gaps.sort()
        before = startTime[0]
        for i in range(n):
            meeting_time = endTime[i] - startTime[i]
            after = startTime[i + 1] - endTime[i]
            # put it somewhere else
            index = bisect.bisect_left(gaps, meeting_time)
            gte_gaps = len(gaps) - index
            if before >= meeting_time:
                gte_gaps -= 1
            if after >= meeting_time:
                gte_gaps -= 1
            if gte_gaps > 0:
                max_gap = max(before + meeting_time + after, max_gap)
            # try to put it in the before or after gap
            max_gap = max(before + after, max_gap)

            before = startTime[i + 1] - endTime[i]
        
        return max_gap
