# https://leetcode.com/problems/evaluate-reverse-polish-notation

from collections import deque
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        
        for t in tokens:
            if t == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            elif t == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif t == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)
            elif t == '/':
                a = stack.pop()
                b = stack.pop()
                temp = abs(b) // abs(a)
                stack.append(-temp if (a < 0) ^ (b < 0) else temp)
            else:
                stack.append(int(t))
        
        return stack.pop()

    def evalRPN(self, tokens: list[str]) -> int:
        def evalOperation(a: int, b: int, operation):
            if operation == '+':
                return a + b
            elif operation == '-':
                return a - b
            elif operation == '*':
                return a * b
            else:
                return int(a / b)
            
        stack = deque()

        for token in tokens:
            if not token in '+-*/':
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                result = evalOperation(a, b, token)
                stack.appendleft(result)

        return stack.pop()


