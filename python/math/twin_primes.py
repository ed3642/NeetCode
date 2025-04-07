# https://leetcode.com/problems/closest-prime-numbers-in-range

import math
from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def is_prime(n):
            if n <= 1:
                return False
            if n == 2 or n == 3 or n == 5:
                return True
            if n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
                return False

            sqr = int(math.sqrt(n)) + 2 # +2 to ensure proper range check
            # 6k +/- 1 optimization
            for i in range(6, sqr, 6):
                if n % (i - 1) == 0 or n % (i + 1) == 0:
                    return False
            return True
        
        # 2,3 are a special case
        if left <= 2 and right >= 3:
            return [2, 3]

        temp = -1
        prev = -1
        curr = -1
        for num in range(left, right + 1):
            if is_prime(num):
                prev = temp
                curr = num
                if curr - prev == 2:
                    return [prev, curr] # smallest twin primes
                temp = curr
        
        if prev == -1 or curr == -1 or curr == prev:
            return [-1, -1]
        return [prev, curr]