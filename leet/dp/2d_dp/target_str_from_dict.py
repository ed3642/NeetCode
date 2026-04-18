# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
from functools import lru_cache
from typing import List

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        
        @lru_cache(maxsize=None)
        def ways(word_i, target_i):
            if target_i >= TARGET_I_BOUNDARY:
                return 1 # valid path
            if word_i >= WORD_LENGTH:
                return 0 # invalid path
            
            looking_for = target[target_i]
            available = freqs[word_i][ord(looking_for) - ord('a')]
            take = 0
            if available > 0:
                take = ways(word_i + 1, target_i + 1) * available
            skip = ways(word_i + 1, target_i)

            return take + skip
        
        MOD = (10 ** 9) + 7
        WORD_LENGTH = len(words[0])
        TARGET_I_BOUNDARY = len(target)

        freqs = {i : ([0] * 26) for i in range(WORD_LENGTH)} # freqs[index][char]
        for word in words:
            for i, c in enumerate(word):
                freqs[i][ord(c) - ord('a')] += 1

        return ways(0, 0) % MOD
    