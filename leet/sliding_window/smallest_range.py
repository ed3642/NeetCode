# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
from collections import deque
from typing import List
import heapq

class Solution:
    # NOTE: could reduce the memory like in the LC editorial
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # sliding window with counter
        # window moves by the pointers at each list
        
        N = len(nums)

        merged_list = []
        for level in range(N):
            for val in nums[level]:
                heapq.heappush(merged_list, (val, level))
        
        counts = [0] * N
        missing_levels = N # set([i for i in range(N)]), can just use a count
        start = 0
        end = float('inf')
        q = deque()
        while merged_list:
            val, level = heapq.heappop(merged_list)
            q.append((val, level))
            counts[level] += 1
            if counts[level] == 1:
                missing_levels -= 1
            while missing_levels == 0:
                if q[-1][0] - q[0][0] < end - start:
                    start = q[0][0]
                    end = q[-1][0]
                popped_level = q.popleft()[1]
                counts[popped_level] -= 1
                if counts[popped_level] == 0:
                    missing_levels += 1

        return [start, end]
