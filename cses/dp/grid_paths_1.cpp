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

void solve(vs &grid, int n) {
    
    if (grid[0][0] == '*') {
        cout << 0;
        return;
    }
    
    vector<vector<ll>> dp(n, vector<ll>(n, 0));

    dp[0][0] = 1;
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (grid[i][j] == '.') {
                ll top = (i-1 >= 0 && grid[i-1][j] == '.') ? dp[i-1][j] : 0;
                ll left = (j-1 >= 0 && grid[i][j-1] == '.') ? dp[i][j-1] : 0;
                dp[i][j] = (dp[i][j]+top+left) % MOD;
            }
        }
    }

    cout << dp[n-1][n-1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vs grid(n);
    for (int i = 0; i < n; i++) {
        cin >> grid[i];
    }

    solve(grid, n);

    return 0;
}
