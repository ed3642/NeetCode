# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs

from collections import defaultdict
from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(num):
            # remove trailling 0s
            while num % 10 == 0:
                num //= 10
            rev = 0
            while num:
                d = num % 10
                rev *= 10
                rev += d
                num //= 10
            return rev 

        last_seen = {}

        min_dist = float('inf')
        for i, num in enumerate(nums):
            if num in last_seen:
                min_dist = min(i - last_seen[num], min_dist)
            last_seen[reverse(num)] = i
        
        return min_dist if min_dist != float('inf') else -1

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        # returns the first i where arr[i] >= t, so the first biggest if target not found
        def bisect_left(arr, t):
            l = 0
            r = len(arr)

            while l < r:
                m = (l + r) // 2
                if arr[m] < t:
                    l = m + 1
                else:
                    r = m
            return l
        
        def reverse(num):
            # remove trailling 0s
            while num % 10 == 0:
                num //= 10
            rev = 0
            while num:
                d = num % 10
                rev *= 10
                rev += d
                num //= 10
            return rev 
        
        n = len(nums)
        rev = [0] * n

        indexes = defaultdict(list)
        for i, num in enumerate(nums):
            rev[i] = reverse(num)
            indexes[num].append(i)

        min_dist = float('inf')
        for i, rev_num in enumerate(rev):
            if rev_num in indexes:
                cand_indexes = indexes[rev_num]
                closest_i = bisect_left(cand_indexes, i)
                if closest_i >= len(cand_indexes):
                    continue
                right = cand_indexes[closest_i]
                if right == i: # palindrone -> look at next match
                    if closest_i + 1 < len(cand_indexes):
                        right_2 = cand_indexes[closest_i + 1]
                        cand = right_2 - i
                        if cand > 0:
                            min_dist = min(cand, min_dist)
                else:
                    cand = right - i
                    if cand > 0:
                        min_dist = min(cand, min_dist)

        return min_dist if min_dist != float('inf') else -1