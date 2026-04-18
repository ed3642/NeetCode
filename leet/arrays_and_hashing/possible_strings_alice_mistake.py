# https://leetcode.com/problems/find-the-original-typed-string-i

class Solution:
    def possibleStringCount(self, word: str) -> int:
        
        n = len(word)
        possible_fakes = 0

        for i in range(1, n):
            if word[i] == word[i - 1]:
                possible_fakes += 1
        
        return possible_fakes + 1