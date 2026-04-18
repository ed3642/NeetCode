# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii

import bisect
from functools import lru_cache
from typing import List

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        
        @lru_cache(maxsize=None)
        def max_val(i, left):
            if left == 0 or i >= N:
                return 0
            
            # interestinly putting the skip path first in max() is noticeably faster
            # could be 
            # 1. b/c skip will record more memos that the take path will need
            # 2. the take branch will skip subproblems eratically that others will need
            return max(
                max_val(i + 1, left), # skip
                max_val(next_open[i], left - 1) + events[i][2] # take
                )
        
        N = len(events)
        events.sort(key=lambda x: x[0])
        starts = [events[i][0] for i in range(N)]
        next_open = [bisect.bisect_left(starts, events[i][1] + 1) for i in range(N)]
        return max_val(0, k)

s = Solution()
print(s.maxValue([[1,2,4],[3,4,3],[2,3,10]], 2))