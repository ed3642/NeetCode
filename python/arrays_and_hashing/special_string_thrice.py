# https://leetcode.com/problems/find-longest-special-substring-that-occurs-thrice-i
from collections import defaultdict

class Solution:

    # O(n^2)
    def maximumLength(self, s: str) -> int:
        
        # count the number of substrings, see which one occurs 3 times and is the longest
        # store in hashma in O(1) by nothing generating the whole string
        N = len(s)
        counts = defaultdict(int) # (char, length) : count

        for end in range(1, N + 1):
            for start in range(end - 1, -1, -1):
                if s[start] != s[end - 1]:
                    # one of the letters isnt the same
                    break
                length = end - start
                counts[(s[start], length)] += 1

        longest_len = -1
        for (ch, length), count in counts.items():
            if count > 2:
                longest_len = max((length), longest_len)
        
        return longest_len

    # O(n^3)
    def maximumLength(self, s: str) -> int:
        
        # count the number of substrings, see which one occurs 3 times and is the longest
        N = len(s)
        counts = defaultdict(int)

        for end in range(1, N + 1):
            for start in range(end - 1, -1, -1):
                if s[start] != s[end - 1]:
                    # one of the letters isnt the same
                    break
                counts[s[start:end]] += 1

        longest_len = -1
        for string, count in counts.items():
            if count > 2:
                longest_len = max(len(string), longest_len)
        
        return longest_len