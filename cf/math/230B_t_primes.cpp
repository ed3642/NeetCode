// command to mimic CF run
// g++ -std=gnu++23 -O2 -Wall main.cpp -o main.exe && gc input | .\main.exe

#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vi = vector<int>;
using vd = vector<double>;
using vll = vector<ll>;
using vc = vector<char>;
using vs = vector<string>;
using vvi = vector<vector<int>>;
using pii = pair<int, int>;
using t3 = tuple<int, int, int>;
const ll MOD = 1e9+7;
const ll INF = LLONG_MAX;

inline vi rints(int n) { vi v(n); for (int &x : v) cin >> x; return v; }
inline vll rlls(int n) { vll v(n); for (ll &x : v) cin >> x; return v; }
inline vc rchars(int n) { vc v(n); for (char &c : v) cin >> c; return v; }
inline string rstring() { string s; cin >> s; return s; }
inline vs rall() { vs v; for (string s; cin >> s; ) v.push_back(s); return v; }
inline int vMin(const vi& v) { return *min_element(v.begin(), v.end()); }
inline int vMax(const vi& v) { return *max_element(v.begin(), v.end()); }

void solve(const vll& nums, vi& primes) {
    /*
    This is faster than the tutorial solution in practice but slower on paper.
    This is O(m log log m + n log p) however p < 10^6
    The tutorial is O(m log log m + n) but it has heavy hashing.
    
    look at divisors of n
    n => a b c 
    n => 1 p x (3rd divisor has to be a prime otherwise its also divisible by the components of the non prime)

    4 9 25 49 121 169 289 361 529 841 961 
    2 3 5  7  11  13  17  19  23  29  31

    let p be some prime.
    if n = p*p
    then the only numbers that divide it are {1, p, p*p}.
    since no x divides p*p that is not in that set.
    */

    int primesSz = primes.size();

    for (ll num : nums) {
        int start = lower_bound(primes.begin(), primes.end(), (int) floor(sqrt(num))) - primes.begin();
        if (start >= primesSz) {
            cout << "NO" << '\n';
            continue;
        }
        bool found = false;
        for (int i = start; i < primesSz; i++) {
            int p = primes[i];
            if ((ll) p*p == num) {
                found = true;
                cout << "YES" << '\n';
                break;
            }
            if ((ll) p*p > num) {
                break;
            }
        }
        if (!found)
            cout << "NO" << '\n'; // didnt find a valid prime
    }
    
}

vi sieve(int n) {
    // sieve of eratosthenes
    vi primes;
    vector<bool> isPrime(n+1, true);

    for (int i = 2; i*i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i*i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }

    for (int i = 2; i <= n; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
        }
    }

    return primes;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vll nums = rlls(n);
    ll maxNum = *max_element(nums.begin(), nums.end());
    int maxCheck = (int) ceil(sqrt(maxNum));

    vi primes = sieve(maxCheck);

    solve(nums, primes);

    return 0;
}
