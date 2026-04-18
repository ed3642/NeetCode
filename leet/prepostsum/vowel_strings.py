# https://leetcode.com/problems/count-vowel-strings-in-ranges/
from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        # ["aba","bcb","ece","aa","e"]
        #   [1,0,1,1,1]
        # [0,1,1,2,3,4]

        VOWELS = set('aeiou')
        N = len(words)
        valid_pf_sum = [0] * (N + 1)

        for i, word in enumerate(words):
            if word[0] in VOWELS and word[-1] in VOWELS:
                valid_pf_sum[i + 1] += 1
            valid_pf_sum[i + 1] += valid_pf_sum[i]
        
        res = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            res[i] = valid_pf_sum[r + 1] - valid_pf_sum[l]

        return res