# https://leetcode.com/problems/extra-characters-in-a-string/
from functools import lru_cache
from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        min_left = [float('inf')] * (len(s) + 1)
        min_left[len(s)] = 0

        for start in range(len(s) - 1, -1, -1):
            best = float('inf')
            for word in dictionary:
                end = start + len(word)
                if end <= len(s) and s[start:end] == word:
                    best = min(min_left[end], best)
            # if couldnt find a match starting at this index, +1
            min_left[start] = min(min_left[start + 1] + 1, best)
            
        return min_left[0]

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        @lru_cache(maxsize=None)
        def min_left(start):
            if start >= len(s):
                return 0
            
            best = float('inf')
            for word in dictionary:
                end = start + len(word)
                if end <= len(s) and s[start:end] == word:
                    best = min(min_left(end), best)
            # if couldnt find a match starting at this index, +1
            return min(min_left(start + 1) + 1, best)
            
        return min_left(0)
