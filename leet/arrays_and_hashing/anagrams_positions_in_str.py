# https://leetcode.com/problems/find-all-anagrams-in-a-string
from collections import Counter, defaultdict
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        if len(s) < len(p):
            return []

        N = len(s)
        matches = defaultdict(int)
        target_count = Counter(p)
        matches_needed = len(p)
        l = 0
        res = []

        # initial window
        for r in range(len(p)):
            c = s[r]
            if matches[c] < target_count[c]:
                matches_needed -= 1
            matches[c] += 1
        
        if matches_needed == 0:
            res.append(l)

        for r in range(len(p), N):
            # remove last
            matches[s[l]] -= 1
            if matches[s[l]] < target_count[s[l]]:
                matches_needed += 1
            l += 1

            # add next
            matches[s[r]] += 1
            if matches[s[r]] <= target_count[s[r]]:
                matches_needed -= 1
            
            if matches_needed == 0:
                res.append(l)
        
        return res
