# https://leetcode.com/problems/best-sightseeing-pair/submissions/1358410562/

from typing import List

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        
        N = len(values)
        max_score = -float('inf')
        best_right = -float('inf')
        for i in range(N - 1, -1, -1):
            prev_best_right = best_right - 1
            max_score = max(values[i] + prev_best_right, max_score)
            best_right = max(values[i], prev_best_right)

        return max_score

    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        best_val_i = 0
        max_sight = 0

        for i in range(1, len(values)):
            max_sight = max(
                values[best_val_i] + values[i] + (best_val_i - i),
                max_sight)
            if values[best_val_i] + best_val_i < values[i] + i:
                best_val_i = i
            
        return max_sight
    