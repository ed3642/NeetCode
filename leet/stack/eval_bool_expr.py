# https://leetcode.com/problems/parsing-a-boolean-expression/
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        
        # !(|(&(f,t),t))
        # [!,|,&,f,t]

        def eval_expre(counts, logical_op):
            if logical_op == '&':
                if counts['f'] != 0:
                    return 'f'
                return 't'
            elif logical_op == '|':
                if counts['t'] > 0:
                    return 't'
                return 'f'
            return 't' if counts['f'] != 0 else 'f' # for the ! op, should only be 1 t/f

        logical_ops = set(['!', '&', '|'])
        skippable = set(['(', ','])
        stack = []
        
        N = len(expression)
        i = 0
        while i < N:
            token = expression[i]
            i += 1
            if token in skippable:
                continue
            elif token != ')':
                stack.append(token)
            else:
                counts = {'f': 0, 't': 0}
                while stack and stack[-1] not in logical_ops:
                    counts[stack.pop()] += 1
                logical_op = stack.pop()
                stack.append(eval_expre(counts, logical_op))
        
        return False if stack[-1] == 'f' else True