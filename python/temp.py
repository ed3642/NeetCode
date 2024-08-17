from functools import lru_cache


class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:

        MAX_I = len(points)
        MAX_J = len(points[0])
        max_score = [[0 for _ in range(MAX_J)] for _ in range(MAX_I)]

        for i in range(MAX_J):
            max_score[0][i] = points[0][i]

        for row_i in range(1, MAX_I):
            for last_i_chosen in range(MAX_J):
                best = 0
                for i in range(MAX_J):
                    minus = abs(last_i_chosen - i)
                    best = max(
                        max_score[row_i - 1][i] + points[row_i][last_i_chosen] - minus, 
                        best)
                max_score[row_i][last_i_chosen] = best
        
        return max(max_score[MAX_I - 1])

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