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
const ll MOD = 1e9 + 7;
const ll INF = LLONG_MAX;

inline vi rints(int n) { vi v(n); for (int &x : v) cin >> x; return v; }
inline vc rchars(int n) { vc v(n); for (char &c : v) cin >> c; return v; }
inline string rstring() { string s; cin >> s; return s; }
inline vs rall() { vs v; for (string s; cin >> s; ) v.push_back(s); return v; }
inline int vMin(const vi& v) { return *min_element(v.begin(), v.end()); }
inline int vMax(const vi& v) { return *max_element(v.begin(), v.end()); }

void solve(vi diffs, int n, vi queries, int m) {
    vector<ll> res;
    vi maxSeen(n, diffs[0]);
    vll pfs(n+1);

    for (int i = 0; i < n; i++)
        pfs[i+1] = diffs[i];
    for (int i = 2; i <= n; i++)
        pfs[i] += pfs[i-1];
    
    for (int i = 1; i < n; i++) {
        maxSeen[i] = max(diffs[i], maxSeen[i-1]);
    }

    for (int q : queries) {
        int firstgtI = upper_bound(maxSeen.begin(), maxSeen.end(), q) - maxSeen.begin();

        res.push_back(pfs[firstgtI]);
    }

    // out
    for (auto r : res) 
        cout << r << ' ';
    cout << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        int m;
        cin >> n >> m;

        vi diffs = rints(n);
        vi queries = rints(m);
        solve(diffs, n, queries, m);
    }

    return 0;
}
