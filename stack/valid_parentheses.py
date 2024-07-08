from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        brackets = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        openings = set(['{', '[', '('])

        for ch in s:
            if ch in openings:
                stack.append(ch)
            elif not stack or brackets[ch] != stack.pop():
                return False
        
        return len(stack) == 0

    def isValid(self, s: str) -> bool:
        stack = deque()
        left_brackets = {'(', '[', '{'}

        def isPair(left_bracket, right_bracket):
            if left_bracket == '(' and right_bracket != ')':
                return False
            elif left_bracket == '[' and right_bracket != ']':
                return False
            elif left_bracket == '{' and right_bracket != '}':
                return False
            return True

        for bracket in s:
            if bracket in left_brackets:
                stack.append(bracket)
            else: # right bracket
                if len(stack) == 0:
                    return False
                partner = stack.pop()
                if not isPair(partner, bracket):
                    return False
        return len(stack) == 0 # no more brackets to match