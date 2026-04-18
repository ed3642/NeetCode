# https://leetcode.com/problems/valid-parenthesis-string/
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        left_stack = []
        star_stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                left_stack.append(i)
            elif ch == ')':
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
            else: # its a *
                star_stack.append(i)
                
        # see if we can close the remaining left brackets
        while left_stack and star_stack:
            if left_stack[-1] < star_stack[-1]: # the ( is before the *
                left_stack.pop()
                star_stack.pop()
            else:
                return False
        
        return len(left_stack) == 0