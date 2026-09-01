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

void solve(int n) {
    
    // dp[i] -> ways to make sum of i 
    vi dp(n+1, 0);
    dp[0] = 1;

    for (int s = 1; s <= n; s++) {
        for (int ds = 1; ds < 7; ds++) {
            if (s-ds >= 0)
                dp[s] = (dp[s]+dp[s-ds]) % MOD;
        }
    }

    cout << dp[n] % MOD;
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
