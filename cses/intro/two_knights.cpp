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

// O(n)
void solve(ll n) {
    /*
    place 1 knight and see where the other one can go.
    only count squares after (i, j) to not count the same positions multiple times. This would work but it would be O(n^2), need O(n) for this problem.
  
    1 2 3 4  5  6  7   8     n
    0 0 8 24 48 80 120 168   invalid
    0 0 8 16 24 32 40  48    dx
    0 0 1 3  6  10 15  21    num 8s
    => 8 more invalid positions each time

    invalid = prevInvalid + (n-2)*8
    */
    
    ll prevInvalid = 0;
    for (ll x = 1; x <= n; x++) {
        ll xsqr = (x*x);
        ll total = ((xsqr-1)*(xsqr))/2;
        ll invalid = 0;
        if (x > 2) {
            invalid = prevInvalid+(x-2)*8;
            prevInvalid = invalid;
        }
        cout << total-invalid << '\n';
    }
    
    // out
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n;
    cin >> n;

    solve(n);

    return 0;
}
