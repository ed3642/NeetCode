# https://leetcode.com/problems/best-sightseeing-pair/submissions/1358410562/

class Solution:
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
    