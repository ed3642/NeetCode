# https://leetcode.com/problems/freedom-trail

from collections import defaultdict
from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:

        def get_min_turns(start, end):
            left = start if start < end else end
            right = start if start >= end else end

            op1 = right - left
            op2 = left + len(ring) - right

            return min(op1, op2)

        @lru_cache(maxsize=None)
        def min_turns(start, key_i):
            if key_i >= len(key):
                return 0
            
            min_op = float('inf')
            for end in letter_positions[key[key_i]]:
                if start != end:
                    cost = get_min_turns(start, end)
                    min_op = min(min_op, min_turns(end, key_i + 1) + cost)
                else:
                    min_op = min(min_op, min_turns(end, key_i + 1))
            
            return min_op
        
        letter_positions = defaultdict(list)

        for i, c in enumerate(ring):
            letter_positions[c].append(i)

        return min_turns(0, 0) + len(key)