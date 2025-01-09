# https://leetcode.com/problems/string-matching-in-an-array
from typing import List

class Solution:
    # could also do prefix trie for O(n + m^2) solution

    # KMP
    # O(n^2 + m) n=len(words) m=avg_len_word
    def stringMatching(self, words: List[str]) -> List[str]:

        def search(substring, string):
            N = len(string)
            lps = get_lps(substring)
            to_match_i = 0
            for i in range(N):
                while to_match_i > 0 and string[i] != substring[to_match_i]:
                    to_match_i = lps[to_match_i - 1]
                if substring[to_match_i] == string[i]:
                    to_match_i += 1
                if to_match_i == len(substring):
                    return True
            return False

        def get_lps(string):
            N = len(string)
            lps = [0] * (N)
            to_match_i = 0
            for i in range(1, N):
                while to_match_i > 0 and string[i] != string[to_match_i]:
                    to_match_i = lps[to_match_i - 1]
                if string[to_match_i] == string[i]:
                    to_match_i += 1
                lps[i] = to_match_i
            return lps

        N = len(words)
        res = []
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if len(words[i]) > len(words[j]) - 1:
                    continue
                if search(words[i], words[j]):
                    res.append(words[i])
                    break
        return res

    # O(n m^2)
    def stringMatching(self, words: List[str]) -> List[str]:
        
        substrings = set()
        res = []

        for word in words:
            for r in range(len(word)):
                for l in range(r + 1):
                    if not (l == 0 and r == len(word) - 1):
                        substrings.add(word[l:r + 1])

        for word in words:
            if word in substrings:
                res.append(word)
        
        return res