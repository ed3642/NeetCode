class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        
        def generate_primes(n):
            primes = set()
            non_primes = set()
            p = 2
            while p * p <= n:
                if p not in non_primes:
                    primes.add(p)
                    for i in range(p * p, n + 1, p):
                        non_primes.add(i)
                p += 1
            for p in range(p, n + 1):
                if p not in non_primes:
                    primes.add(p)
            return primes

        primes = generate_primes(int(r ** 0.5))
        # good nums from [1-n]
        special_nums = set()
        for p in primes:
            if p * p <= r:
                special_nums.add(p * p)
        
        # all special nums in [l, r]
        special_count = sum(1 for n in special_nums if l <= n and n <= r)

        # the length of the range - the special nums
        return (r - l + 1) - special_count