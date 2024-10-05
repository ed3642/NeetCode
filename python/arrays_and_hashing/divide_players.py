# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
from collections import defaultdict
from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        N = len(skill)
        _sum = sum(skill)
        num_pairs = N // 2
        rem = _sum % (num_pairs)
        if rem != 0:
            return -1
        
        target = _sum // (num_pairs)
        seen = defaultdict(int)
        total_chemistry = 0

        for s in skill:
            need = target - s
            if need in seen:
                total_chemistry += s * need
                seen[need] -= 1
                if seen[need] == 0:
                    del seen[need]
            else:
                seen[s] += 1
        
        return total_chemistry if len(seen) == 0 else -1
    