# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/
# basically identical to https://leetcode.com/problems/valid-parenthesis-string/
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        # ((() (())

        N = len(s)
        if N % 2 != 0:
            return False
        
        left_stack = []
        free_stack = []

        for i, c in enumerate(s):
            if locked[i] == '0':
                free_stack.append(i)
            elif c == '(':
                left_stack.append(i)
            else: # )
                if left_stack:
                    left_stack.pop()
                elif free_stack:
                    free_stack.pop()
                else:
                    return False

        while left_stack and free_stack:
            if left_stack[-1] < free_stack[-1]:
                left_stack.pop()
                free_stack.pop()
            else:
                return False

        return not left_stack
    