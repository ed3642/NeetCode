# https://leetcode.com/problems/partition-labels
from typing import Counter, List

class Solution:
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