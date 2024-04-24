class Solution:
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