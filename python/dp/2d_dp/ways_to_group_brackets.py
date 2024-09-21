from functools import lru_cache
from typing import List

class Solution:
    # hard to intuit
    # break into left and right of each operator and take all combinations of the results from left and right recursively
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def parse_string(string: str):
            N = len(string)
            res = []
            i = 0
            while i < N:
                curr = []
                if string[i] in operators:
                    res.append(string[i])
                    i += 1
                while i < N and string[i].isdigit():
                    curr.append(string[i])
                    i += 1
                if curr:
                    res.append(''.join(curr))
            return res

        @lru_cache(maxsize=None)
        def ways(start, end):
            if start == end:
                return [int(parsed_str[start])]
            
            res = []
            for i in range(start, end + 1):
                if parsed_str[i] in operators:
                    op = parsed_str[i]
                    left = ways(start, i - 1)
                    right = ways(i + 1, end)
                    for left_exp in left:
                        for right_exp in right:
                            if op == '+':
                                res.append(left_exp + right_exp)
                            elif op == '-':
                                res.append(left_exp - right_exp)
                            elif op == '*':
                                res.append(left_exp * right_exp)
            return res

        operators = set('*-+')
        parsed_str = parse_string(expression)
        N = len(parsed_str)

        return ways(0, N - 1)