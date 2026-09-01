import math

class Primes:
    # better way to gen primes, sieve of eratosthenes [2, n]
    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n + 1, i):
                    is_prime[j] = False

        return [i for i in range(2, n + 1) if is_prime[i]]


    def gen_primes(n):
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
    
    # factor nums up to n into their primes in O(n log n)
    # prime factor seive
    def gen_prime_factors(n):
        factors = [[] for _ in range(n)]
        for i in range(2, n):
            if not factors[i]:
                for j in range(i, n, i):
                    factors[j].append(i)
        return factors
    
    # Smallest Prime Factor lets us generate the prime factors of a num x in log x time
    # spf is made in O(n log (log n)) time
    def gen_spf(n):
        # Prime factors of nums are generated as so in O(log num):
        # while num > 1:
        #     g[spf[num]].append(i)
        #     num = num // spf[num]
    
        spf = [i for i in range(n)]

        for i in range(2, int(math.sqrt(n)) + 1):
            if spf[i] == i:
                for j in range(i * i, n, i):
                    if spf[j] == j:
                        spf[j] = i
        return spf