# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        
        builder = []
        _sum = 0

        for x in str(n):
            if x != '0':
                builder.append(x)
                _sum += int(x)
        
        if not builder:
            return 0
        return int(''.join(builder)) * _sum
