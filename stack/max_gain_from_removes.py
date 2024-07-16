import operator

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        # prioritise more expenside op
        # 2 passes

        def process(operator, s):
            prio = 'ab' if operator(x, y) else 'ba'
            prio_val = x if operator(x, y) else y
            score = 0
            stack.clear()

            for ch in s:
                if stack and stack[-1] + ch == prio:
                    stack.pop()
                    score += prio_val
                else:
                    stack.append(ch)
            return score

        stack = []
        max_score = 0
        max_score += process(operator.gt, s) # x > y
        max_score += process(operator.le, ''.join(stack)) # x <= y

        return max_score
