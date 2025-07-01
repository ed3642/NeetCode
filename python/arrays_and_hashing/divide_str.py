# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k

from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        
        res = []

        i = 0
        while i + k <= len(s):
            res.append(s[i:i + k])
            i += k
        
        # no remainder
        if i == len(s):
            return res
        
        # remainder
        need = k - (len(s) - i)
        res.append(s[i:len(s)] + (fill * need))

        return res
    