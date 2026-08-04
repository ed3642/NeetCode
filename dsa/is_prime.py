import math

# O(sqrt n)
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

# O(log n)
def is_prime(n):
    if n < 2:
        return False
    # small primes
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for p in small_primes:
        if n % p == 0:
            return n == p

    # write n-1 = d * 2^s
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2

    # deterministic bases for 64-bit integers
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True
