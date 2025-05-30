# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words

from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        
        size = 0
        freqs = Counter(words)

        for word in freqs:
            pairing = word[1] + word[0]
            if word == pairing:
                can_take = freqs[word] // 2
                freqs[word] -= can_take * 2
                size += can_take * 4
            else:
                if freqs[pairing] >= 1:
                    can_take = min(freqs[word], freqs[pairing])
                    freqs[word] -= can_take
                    freqs[pairing] -= can_take
                    size += can_take * 4
        
        # check for middle
        for word in freqs:
            if word[0] == word[1] and freqs[word] > 0:
                size += 2
                break

        return size