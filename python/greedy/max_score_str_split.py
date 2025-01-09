# https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        
        ones_count = s.count('1')
        max_score = -float('inf')
        score = ones_count
        for i in range(len(s) - 1):
            if s[i] == '0':
                score += 1
            else:
                score -= 1
            max_score = max(score, max_score)
        
        return max_score
