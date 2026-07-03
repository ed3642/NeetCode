# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word

from typing import List

class Solution:

    # O(n m)
    def numOfStrings(self, patterns: List[str], word: str) -> int:

        def kmp(string, pattern):

            def get_lps():
                lps = [0] * M
                
                j = 0
                for i in range(1, M):
                    while j > 0 and pattern[j] != pattern[i]:
                        j = lps[j-1]
                    if pattern[j] == pattern[i]:
                        j += 1
                    lps[i] = j

                return lps
            
            M = len(pattern)
            N = len(string)
            if N == 0 or M == 0:
                return -1

            lps = get_lps()

            j = 0
            for i in range(N):
                while j > 0 and pattern[j] != string[i]:
                    j = lps[j-1]
                if pattern[j] == string[i]:
                    j += 1
                if j == M:
                    return i-j+1
                
            return -1

        c = 0
        for p in patterns:
            if kmp(word, p) != -1:
                c += 1
        return c
    
    # O(n m^2)
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        
        c = 0
        for p in patterns:
            if p in word:
                c += 1
        return c