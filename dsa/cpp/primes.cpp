#include <bits/stdc++.h>
using namespace std;

class Primes {
public:
    // sieve of eratosthenes [2, n] O(n log log n)
    static vector<int> sieve(int n) {
        if (n < 2)
            return {};

        vector<bool> is_prime(n + 1, true);
        is_prime[0] = false;
        is_prime[1] = false;

        for (int i = 2; (long long)i * i <= n; i++) {
            if (is_prime[i]) {
                for (long long j = (long long)i * i; j <= n; j += i) {
                    is_prime[j] = false;
                }
            }
        }

        vector<int> result;
        for (int i = 2; i <= n; i++) {
            if (is_prime[i]) result.push_back(i);
        }
        return result;
    }

    // factor nums up to n into their primes in O(n log log n)
    // prime factor sieve
    static vector<vector<int>> gen_prime_factors(int n) {
        vector<vector<int>> factors(n);
        for (int i = 2; i < n; i++) {
            if (factors[i].empty()) {
                for (int j = i; j < n; j += i) {
                    factors[j].push_back(i);
                }
            }
        }
        return factors;
    }

    // O(sqrt n)
    bool isPrime(int n) {
        if (n < 2) 
            return false;
        if (n == 2 || n == 3)
            return true;
        if (n % 2 == 0 || n % 3 == 0)
            return false;
        
        for (int i = 5; (long long) i*i <= n; i += 6) {
            if (n % (i) == 0 || n % (i+2) == 0) {
                return false;
            } 
        }

        return true;
    }

    // Smallest Prime Factor lets us generate the prime factors of a num x in log x time
    // spf is made in O(n log (log n)) time
    static vector<int> gen_spf(int n) {
        // Prime factors of nums are generated as so in O(log num):
        // while (num > 1) {
        //     g[spf[num]].push_back(i);
        //     num = num / spf[num];
        // }

        vector<int> spf(n);
        for (int i = 0; i < n; i++) spf[i] = i;

        for (int i = 2; (long long)i * i <= n; i++) {
            if (spf[i] == i) {
                for (int j = i * i; j < n; j += i) {
                    if (spf[j] == j) {
                        spf[j] = i;
                    }
                }
            }
        }
        return spf;
    }
};