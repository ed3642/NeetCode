# https://leetcode.com/problems/count-good-numbers

from functools import lru_cache

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # there is a better "fast exponentiation" algo but im not interested
        
        # need to break up power calculations, try exponent basecase is less than 5000
        # EOEOEOE
        # 0,2,4,6,8 evens
        # 2,3,5,7 odds are primes
        # 5, 20, 100, 400, 2000

        @lru_cache(maxsize=None)
        def calculate(m, exp):
            if exp < 12:
                # should be small enough to calculate
                return (m ** exp)
            
            first_split = (exp // 2)
            second_split = ((exp + 1) // 2)

            return (calculate(m, first_split) * calculate(m, second_split)) % MOD

        MOD = 10 ** 9 + 7
        odds = (n // 2)
        evens = ((n + 1) // 2)
        odd_val = max(calculate(4, odds), 1) % MOD
        even_val = calculate(5, evens) % MOD

        return (even_val * odd_val) % MOD

