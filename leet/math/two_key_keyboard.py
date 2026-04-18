# https://leetcode.com/problems/2-keys-keyboard/
from functools import lru_cache

class Solution:
    # O(n) voodo solution
    # problem transformed into finding all prime factors of n
    def minSteps(self, n: int) -> int:
        d = 2
        operations = 0
    
        while n > 1:
            # While d is a prime factor of n
            while n % d == 0:
                operations += d  # Add d to the operations count (d operations needed)
                n //= d  # Remove the factor d from n
            d += 1  # Increment d to check the next potential prime factor
            # No composite number will divide n since all smaller prime factors have been removed
    
        return operations

    def minSteps(self, n: int) -> int:
        
        # O(n^2)
        @lru_cache(maxsize=None)
        def min_ops(num, copied):
            if num > n:
                return float('inf')
            if num == n:
                return 0
            
            # only copy if we didnt copy last operation
            if copied == num:
                return min_ops(num + copied, copied) + 1 # paste
            
            return min(
                min_ops(num, num), # copy
                min_ops(num + copied, copied) # paste
            ) + 1

        if n == 1:
            return 0
        return min_ops(1, 1) + 1