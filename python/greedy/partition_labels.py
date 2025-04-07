# https://leetcode.com/problems/partition-labels
from typing import Counter, List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        counts = Counter(s)
        res = []
        current_size = 0
        in_window = set()

        for c in s:
            current_size += 1
            counts[c] -= 1
            in_window.add(c)

            if counts[c] == 0:
                in_window.remove(c)
                if len(in_window) == 0:
                    res.append(current_size)
                    current_size = 0
        
        return res

    def partitionLabels(self, s: str) -> List[int]:
        
        counts = Counter(s)
        res = []

        i = 0
        while i < len(s):
            to_find = set([s[i]])
            length = 0
            while to_find:
                to_find.add(s[i])
                counts[s[i]] -= 1
                if counts[s[i]] == 0:
                    to_find.remove(s[i])
                length += 1
                i += 1
            res.append(length)
        
        return res