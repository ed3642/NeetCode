# https://leetcode.com/problems/russian-doll-envelopes

from bisect import bisect_left
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        # [[5,4],[6,4],[6,7],[2,3],[4,5]]
        # [2,5,4,6,6] len(LIS) = 3
        # reframe question to the non intersecting segments problem
        # which can be solved by getting the LIS of arr where arr is the elem[0] of each interval after sorting the elems by elem[1]
        if len(envelopes) == 1: return 1
        envelopes.sort(key=lambda x: (x[1], -x[0]))
        arr = [w for (w, _) in envelopes]
        
        lis = []

        for w in arr:
            placer_i = bisect_left(lis, w)
            if placer_i == len(lis):
                lis.append(w)
            else:
                lis[placer_i] = w
        
        return len(lis)
