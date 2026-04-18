# https://leetcode.com/problems/solving-questions-with-brainpower

from functools import lru_cache
from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @lru_cache(maxsize=None)
        def max_score(i):
            if i >= len(questions):
                return 0
            if i == len(questions) - 1:
                return questions[i][0] # always take last option

            return max(
                max_score(i + questions[i][1] + 1) + questions[i][0], 
                max_score(i + 1)
            )
        
        return max_score(0)