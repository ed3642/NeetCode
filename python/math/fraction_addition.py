# https://leetcode.com/problems/fraction-addition-and-subtraction/
from functools import reduce

class Solution:
    def fractionAddition(self, expression: str) -> str:

        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)
        
        def sum_fractions(a, b):
            top1 = a[0]
            top2 = b[0]
            bot1 = a[1]
            bot2 = b[1]
            if bot1 != bot2:
                return ((top1 * bot2) + (top2 * bot1), bot1 * bot2)
            return (top1 + top2, bot1)

        def build_num(i):
            num_builder = []
            while i < N and expression[i].isdigit():
                num_builder.append(expression[i])
                i += 1
            return int(''.join(num_builder)), i

        fractions = []

        N = len(expression)
        i = 0
        # parse the string into easy to work with tuples that represent each fraction
        while i < N:
            sign = 1 # 1 for +, -1 for -
            # get the sign
            if expression[i] == '-':
                sign = -1
                i += 1
            elif expression[i] == '+':
                i += 1
            # get the top
            top, i = build_num(i)
            i += 1
            # get the bot
            bot, i = build_num(i)
            fractions.append((sign * top, bot))
        
        # sums up all the fractions
        final_top, final_bot = reduce(sum_fractions, fractions)
        sign = ''
        if final_top < 0:
            sign = '-'
            final_top *= -1
        _gcd = gcd(final_top, final_bot)
        final_top //= _gcd
        final_bot //= _gcd
        return f'{sign}{final_top}/{final_bot}'