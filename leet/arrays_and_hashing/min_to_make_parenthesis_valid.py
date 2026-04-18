# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        lefts = 0
        need = 0
        for c in s:
            if c == '(':
                lefts += 1
            else:
                if lefts > 0:
                    lefts -= 1
                else:
                    need += 1
        
        return lefts + need