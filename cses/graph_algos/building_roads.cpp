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

void dfs(vvi &g, vi &visited, int node) {
    visited[node] = true;

    for (int nei: g[node]) {
        if (!visited[nei]) {
            dfs(g, visited, nei);
        }
    }
}

void solve(vector<pii> &edges, int n) {
    /*
    dfs to see how many groups there are and we need groups-1 new roads.

    cities are 1 to n
    */
    
    vvi g(n+1);
    vi firstSeenInGroup;
    vi visited(n+1);

    for (auto [u, v] : edges) {
        g[u].push_back(v);
        g[v].push_back(u);
    }

    for (int i = 1; i <= n; i++) {
        if (!visited[i]) {
            firstSeenInGroup.push_back(i);
            dfs(g, visited, i);
        }
    }

    int roadsNeeded = firstSeenInGroup.size()-1;
    cout << roadsNeeded << '\n';
    for (int i = 1; i <= roadsNeeded; i++) {
        cout << firstSeenInGroup[i-1] << ' ' << firstSeenInGroup[i] << '\n';
    }
    // out
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int m;
    cin >> n >> m;

    vector<pii> edges(m);
    for (int i = 0; i < m; i++) {
        cin >> edges[i].first >> edges[i].second;
    }

    solve(edges, n);

    return 0;
}
