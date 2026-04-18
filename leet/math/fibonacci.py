# https://leetcode.com/problems/fibonacci-number

class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        f = 1
        f_i_minus_1 = 1
        f_i_minus_2 = 0

        for _ in range(2, n + 1):
            f = f_i_minus_1 + f_i_minus_2
            f_i_minus_2, f_i_minus_1 = f_i_minus_1, f
        
        return f

    def fib(self, n: int) -> int:

        if n == 0:
            return 0
        if n == 1:
            return 1
        
        f = [0] * (n + 1)
        f[1] = 1

        for i in range(2, n + 1):
            f[i] = f[i - 2] + f[i - 1]
        
        return f[n]
    
    def __init__(self):
        self.memo = {}

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        ans = None
        if n in self.memo:
            return self.memo[n]
        else:
            ans = self.fib(n - 1) + self.fib(n - 2)
            self.memo[n] = ans
        
        return ans