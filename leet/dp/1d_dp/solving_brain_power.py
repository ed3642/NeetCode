# https://leetcode.com/problems/solving-questions-with-brainpower

from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions) # biggest question index + skip can be 
        dp = [0 for _ in range(n + 1)]

        for i, (points, skip) in enumerate(questions):
            next_i = i+skip+1
            if next_i < n:
                dp[next_i] = max(dp[i]+points, dp[next_i])
            else:
                dp[n] = max(dp[i]+points, dp[n]) # use the nth index as a way to keep track of the best score that goes beyond n - 1
            dp[i+1] = max(dp[i], dp[i+1])

        return dp[n]