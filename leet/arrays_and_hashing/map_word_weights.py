# https://leetcode.com/problems/weighted-word-mapping

from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        n = len(words)
        res = [''] * n

        for i in range(n):
            _sum = 0
            for c in words[i]:
                _sum += weights[ord(c)-ord('a')]
            _sum %= 26
            res[i] = chr(25-_sum+ord('a'))

        return ''.join(res)