# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array

from typing import List

class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        n = len(words)
        i = startIndex
        steps = 0
        op1 = float('inf')
        while steps < n:
            if words[i] == target:
                op1 = steps
                break
            i = (i + 1) % n
            steps += 1

        if op1 == float('inf'):
            return -1

        i = startIndex
        steps = 0
        while True:
            if words[i] == target:
                return min(op1, steps)
            i = (i - 1 + n) % n
            steps += 1
        