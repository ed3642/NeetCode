# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks

from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        tasks.sort(key=lambda x: -(x[1] - x[0]))

        total = 0
        curr_e = 0
        for cost, min_e in tasks:
            need = min_e - curr_e
            if need > 0:
                total += need
                curr_e += need
            curr_e -= cost
        
        return total