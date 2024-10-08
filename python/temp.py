# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
class Solution:
    def minSwaps(self, s: str) -> int:
        
        lefts = 0
        mismatches = 0
        for c in s:
            if c == '[':
                lefts += 1
            else:
                if lefts > 0:
                    lefts -= 1
                else:
                    mismatches += 1
        
        return (mismatches + 1) // 2

    def minSwaps(self, s: str) -> int:
        
        lefts = 0
        rights = 0
        mismatches = 0
        for c in s:
            if c == ']':
                rights += 1
            elif c == '[':
                lefts += 1
            if rights > lefts:
                mismatches = max(rights - lefts, mismatches)
        
        return mismatches // 2 if mismatches % 2 == 0 else mismatches // 2 + 1
