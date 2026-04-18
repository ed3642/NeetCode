# https://leetcode.com/problems/number-of-atoms/
from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:

        def build_name(i):
            builder = [formula[i]]
            i += 1
            while i < len(formula) and formula[i].islower():
                builder.append(formula[i])
                i += 1
            return (''.join(builder), i) # name, end_index
        
        def build_mult(i):
            builder = []
            while i < len(formula) and formula[i].isnumeric():
                builder.append(formula[i])
                i += 1
            mult = int(''.join(builder)) if len(builder) > 0 else 1
            return (mult, i) # mult, end_index
        
        stack = [defaultdict(int)]
        n = len(formula)
        i = 0
        while i < n:
            if formula[i] == '(': # put them into the stack
                stack.append(defaultdict(int))
                i += 1

            elif formula[i] == ')':
                i += 1 # skip ) were on
                mult, i = build_mult(i)
                multiplied_elems = stack.pop()

                for name, count in multiplied_elems.items():
                    stack[-1][name] += count * mult

            else: # process it directly into main dict
                elem, i = build_name(i)
                mult, i = build_mult(i)
                stack[-1][elem] += mult
        
        # format output
        res = []
        for name, count in stack[-1].items():
            res.append((name, count))
        res.sort(key=lambda x: x[0])
        tokens = []
        for name, count in res:
            if count > 1:
                tokens.append(f'{name}{str(count)}')
            else:
                tokens.append(f'{name}')

        return ''.join(tokens)
    