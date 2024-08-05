import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        l = 0
        r = x // 2
        while l <= r:
            m = (l + r) // 2
            sqr = m * m
            if sqr < x:
                l = m + 1
            elif sqr > x:
                r = m - 1
            else:
                return m
        return l if l < r else r
    
    # Newtons method
    # x = 1/2 * (x + a/x) with 0.1 err
    def mySqrt2(self, x: int) -> int:
        newton_iter = lambda x, a: 0.5 * (x + a / x)
        a = x
        prev = 0
        while abs(prev - x) > 0.1:
            prev = x
            x = newton_iter(x, a)
        return math.floor(x)

s = Solution()
print(s.mySqrt2(1000000))
