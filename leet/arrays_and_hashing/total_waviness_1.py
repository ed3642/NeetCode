# https://leetcode.com/problems/total-waviness-of-numbers-in-range-i

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        # there is a digit dp solution but this will do for these constraints, dp or better solution is needed for hard version of this problem

        def count(digits):
            n = len(digits)

            total = 0

            for i in range(1, n-1):
                if digits[i-1] < digits[i] > digits[i+1]:
                    total += 1
                elif digits[i-1] > digits[i] < digits[i+1]:
                    total += 1
            return total
            
        res = 0
        for n in range(num1, num2+1):
            res += count([int(d) for d in str(n)])
        return res