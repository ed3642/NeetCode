#include <bits/stdc++.h>
using namespace std;

// O(sqrt n)
bool is_prime_sqrt(long long n) {
    if (n <= 1) return false;
    if (n == 2 || n == 3 || n == 5) return true;
    if (n % 2 == 0 || n % 3 == 0 || n % 5 == 0) return false;

    long long sqr = (long long)sqrt((double)n) + 2; // +2 to ensure proper range check
    // 6k +/- 1 optimization
    for (long long i = 6; i < sqr; i += 6) {
        if (n % (i - 1) == 0 || n % (i + 1) == 0) return false;
    }
    return true;
}

// modular multiplication and exponentiation using __int128 to avoid overflow
static long long mulmod(long long a, long long b, long long m) {
    return (long long)(((__int128)a * b) % m);
}

static long long powmod(long long a, long long d, long long n) {
    long long result = 1 % n;
    a %= n;
    while (d > 0) {
        if (d & 1) result = mulmod(result, a, n);
        a = mulmod(a, a, n);
        d >>= 1;
    }
    return result;
}

// O(log n) — deterministic Miller-Rabin for 64-bit integers
bool is_prime(long long n) {
    if (n < 2) return false;

    // small primes
    static const int small_primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    for (int p : small_primes) {
        if (n % p == 0) return n == p;
    }

    // write n-1 = d * 2^s
    long long d = n - 1;
    int s = 0;
    while (d % 2 == 0) {
        s++;
        d /= 2;
    }

    // deterministic bases for 64-bit integers
    static const long long bases[] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022};
    for (long long a : bases) {
        if (a % n == 0) continue;
        long long x = powmod(a, d, n);
        if (x == 1 || x == n - 1) continue;

        bool composite = true;
        for (int i = 0; i < s - 1; i++) {
            x = mulmod(x, x, n);
            if (x == n - 1) {
                composite = false;
                break;
            }
        }
        if (composite) return false;
    }
    return true;
}