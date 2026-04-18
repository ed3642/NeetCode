# https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i

from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        
        l = 0

        # stopper
        n = len(startTime)
        startTime.append(eventTime)
        endTime.append(eventTime)
        curr_free_time = startTime[0] # 0 to first meeting
        
        for i in range(k):
            curr_free_time += startTime[i + 1] - endTime[i] # after meeting
        max_free_time = curr_free_time
        
        for r in range(k, n):
            # free time before meeting leaving window
            if l == 0:
                curr_free_time -= startTime[l]
            else:
                curr_free_time -= startTime[l] - endTime[l - 1]
            l += 1

            curr_free_time += startTime[r + 1] - endTime[r] # after meeting
            max_free_time = max(curr_free_time, max_free_time)

        return max_free_time
