from collections import deque

class Solution:
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


