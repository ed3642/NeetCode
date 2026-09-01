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

int dfs(vvi &g, vi &subs, int node) {

    for (int nei : g[node]) {
        subs[node] += dfs(g, subs, nei);
    }

    return subs[node]+1;
}

void solve(vi &parent, int n) {
    
    vvi g(n+1);
    vi subs(n+1, 0);
    
    for (int i = 0; i < n-1; i++) {
        g[parent[i]].push_back(i+2);
    }

    subs[1] = dfs(g, subs, 1)-1;
    
    // out
    for (int i = 1; i <= n; i++) {
        cout << subs[i] << ' ';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vi parent = rvec<int>(n);
    solve(parent, n);

    return 0;
}
