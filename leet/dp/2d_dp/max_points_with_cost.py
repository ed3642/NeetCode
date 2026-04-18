# https://leetcode.com/problems/maximum-number-of-points-with-cost/
from functools import lru_cache

class Solution:
    # key insight: we dont have to calc the score for the cell were on for each
    # different last_i_chosen i. We can make a prefix and postfix of the values
    # and calc the score of the entire row in O(n) instead of O(n^2)
    def maxPoints(self, points: list[list[int]]) -> int:

        MAX_I = len(points)
        MAX_J = len(points[0])
        max_score = points

        for i in range(MAX_J):
            max_score[MAX_I - 1][i] = points[MAX_I - 1][i]

        for i in range(MAX_I - 2, -1, -1):

            for j in range(1, MAX_J):
                max_score[i + 1][j] = max(max_score[i + 1][j - 1] - 1, max_score[i + 1][j])
            for j in range(MAX_J - 2, -1, -1):
                max_score[i + 1][j] = max(max_score[i + 1][j + 1] - 1, max_score[i + 1][j])
            
            for j in range(MAX_J):
                max_score[i][j] += max_score[i + 1][j]

        return max(max_score[0])

    # this works but could still have some optimizations, it showcases the main optimization needed
    # of updating each row in the dp in O(n)
    def maxPoints(self, points: list[list[int]]) -> int:

        MAX_I = len(points)
        MAX_J = len(points[0])
        max_score = [[0 for _ in range(MAX_J)] for _ in range(MAX_I)]

        for i in range(MAX_J):
            max_score[MAX_I - 1][i] = points[MAX_I - 1][i]

        for i in range(MAX_I - 2, -1, -1):
            prefix = max_score[i + 1].copy()
            postfix = max_score[i + 1].copy()

            for j in range(1, MAX_J):
                prefix[j] = max(prefix[j - 1] - 1, max_score[i + 1][j])
            for j in range(MAX_J - 2, -1, -1):
                postfix[j] = max(postfix[j + 1] - 1, max_score[i + 1][j])
            
            for j in range(MAX_J):
                max_score[i][j] = points[i][j] + max(prefix[j], postfix[j])

        return max(max_score[0])

    # too slow, one too many embedded loops
    def maxPoints(self, points: list[list[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def max_score(row_i, last_i_chosen):
            if row_i >= len(points):
                return 0
            
            best = 0
            for i in range(len(points[0])):
                minus = 0
                if last_i_chosen != -1:
                    minus = abs(last_i_chosen - i)
                best = max(
                    max_score(row_i + 1, i) + (points[row_i][i] - minus),
                    best)
            
            return best

        return max_score(0, -1)