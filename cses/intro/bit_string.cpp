// command to run test
// g++ -std=gnu++23 -O2 -Wall main.cpp -o main.exe && gc input | .\main.exe

#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using vi = vector<int>;
using vd = vector<double>;
using vll = vector<ll>;
using vc = vector<char>;
using vs = vector<string>;
using vb = vector<bool>;
using vvi = vector<vector<int>>;
using pii = pair<int, int>;
using t3 = tuple<int, int, int>;
const ll MOD = 1e9+7;
const ll INF = LLONG_MAX;

template <typename T> vector<T> rvec(int n) { vector<T> v(n); for (T &x : v) cin >> x; return v; }

void solve(int n) {
    /*
    need to do fast exponentiation does x^n in O(log n)

    example:
    13 -> 1101
    x^13 = x^8 * x^4 * x^1
    */
    
    ll s = 1;
    ll base = 2;

    while (n > 0) {
        //cout << s << '\n';
        if (n & 1) {
            s = (s*base) % MOD;
        }
        base = (base * base) % MOD;
        n = n >> 1;
    }
    
    cout << s;
    // out
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    solve(n);

    return 0;
}
