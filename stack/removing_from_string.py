class Solution:
    def removeStars(self, s: str) -> str:
        # add to stack from left and just pop when you see a *

        stack = []

        for ch in s:
            if ch == '*':
                stack.pop()
            else:
                stack.append(ch)
        
        return ''.join(stack)