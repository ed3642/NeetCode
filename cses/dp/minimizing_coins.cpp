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
const int INF = INT32_MAX;

template <typename T> vector<T> rvec(int n) { vector<T> v(n); for (T &x : v) cin >> x; return v; }

void solve(vi &coins, int n, int target) {
    /*
    dp
    */
    
    // dp[i] -> the min coins needed to get sum i
    vi dp(target+1, INF);

    // takes 1 coin to make each coin
    for (int coin : coins) {
        if (coin <= target)
            dp[coin] = 1;
    }

    for (int s = 1; s <= target; s++) {
        for (int coin : coins) {
            int prevS = s-coin;
            if (0 < prevS && prevS < target && dp[prevS] != INF)
                dp[s] = min(dp[s], dp[s-coin]+1);
        }
    }

    if (dp[target] == INF) {
        cout << -1;
        return;
    }
    cout << dp[target];
    // out
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    int target;
    cin >> n >> target;
    
    vi coins = rvec<int>(n);

    solve(coins, n, target);

    return 0;
}
