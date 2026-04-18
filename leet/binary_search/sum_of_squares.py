import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        l = 0
        r = math.floor(math.sqrt(c))

        while l <= r:
            curr = l ** 2 + r ** 2
            if curr > c:
                r -= 1
            elif curr < c:
                l += 1
            else:
                return True
        return False