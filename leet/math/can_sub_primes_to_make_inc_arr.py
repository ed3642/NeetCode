# https://leetcode.com/problems/prime-subtraction-operation
from typing import List
import bisect

class Solution:

    # reuse generated primes
    primes = []
    def __init__(self):
        if not Solution.primes:
            Solution.primes = self.generate_primes(1000)

    def primeSubOperation(self, nums: List[int]) -> bool:

        N = len(nums)
        if N == 1:
            return True

        for i in range(N - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                # look for prime to subtract
                prime_i = bisect.bisect_left(Solution.primes, nums[i] - nums[i + 1] + 1)
                if prime_i >= len(Solution.primes):
                    return False
                nums[i] -= Solution.primes[prime_i]
                if nums[i] <= 0:
                    return False
                
        return True
    
    # max num exclusive
    def generate_primes(self, max_num):
        primes = set()
        non_primes = set()

        p = 2
        while p * p <= max_num:
            if p not in non_primes:
                primes.add(p)
                for n in range(p * p, max_num, p):
                    non_primes.add(n)
            p += 1
        for n in range(p, max_num):
            if n not in non_primes:
                primes.add(n)
        return sorted(primes)