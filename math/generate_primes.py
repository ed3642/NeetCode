# seive of eratosthenes for generating primes from [2, n]
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