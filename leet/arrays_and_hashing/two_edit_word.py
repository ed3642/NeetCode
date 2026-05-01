# https://leetcode.com/problems/words-within-two-edits-of-dictionary

from typing import List

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        
        def can_match(word):
            n = len(word)
            for match in dictionary:
                misses = 0
                if len(match) == n:
                    for i in range(n):
                        if match[i] != word[i]:
                            misses += 1
                            if misses > 2:
                                break
                if misses <= 2:
                    return True
            return False


        res = []
        for word in queries:
            if can_match(word):
                res.append(word)
        
        return res