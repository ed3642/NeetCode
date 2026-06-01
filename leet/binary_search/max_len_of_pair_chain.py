# https://leetcode.com/problems/maximum-length-of-pair-chain

from bisect import bisect_left
from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # non intersecting segments problem
        
        pairs.sort(key=lambda x: (x[1], x[0]))
        arr = [pairs[0][0]]
        last_r = pairs[0][1]
        for l, r in pairs:
            if l > last_r:
                arr.append(r)
                last_r = r

        lis = []
        for num in arr:
            placer_i = bisect_left(arr, num)
            if placer_i == len(lis):
                lis.append(num)
            else:
                lis[placer_i] = num
        return len(lis)
