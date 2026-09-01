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
using vb = vector<bool>;
using vvi = vector<vector<int>>;
using pii = pair<int, int>;
using t3 = tuple<int, int, int>;
const ll MOD = 1e9+7;
const ll INF = LLONG_MAX;

template <typename T> vector<T> rvec(int n) { vector<T> v(n); for (T &x : v) cin >> x; return v; }

void solve(int i, int j) {
    /*
    even x goes down
    odd x goes up

    1-indexed
    */
    
    if (j > i) { // col dominant
        if (j % 2 == 0) {
            ll prevSqr = (ll) (j-1)*(j-1);
            cout << prevSqr+i << '\n';
            return;
        } else {
            ll sqr = (ll) j*j;
            cout << sqr-i+1 << '\n';
            return;
        }
    } else { // row dominant
        if (i % 2 == 0) {
            ll sqr = (ll) i*i;
            cout << sqr-j+1 << '\n';
            return;
        } else {
            ll prevSqr = (ll) (i-1)*(i-1);
            cout << prevSqr+j << '\n';
            return;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int i;
        int j; 
        cin >> i >> j;
        solve(i, j);
    }

    return 0;
}
