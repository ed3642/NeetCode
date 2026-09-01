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

vi arr;

bool works(ll m, int n, ll hp) {
    ll dmg = 0;
    for (int i = 1; i < n; i++) {
        dmg += min({(ll) arr[i]-arr[i-1], m});
        if (dmg >= hp) 
            return true;
    }
    dmg += m;
    if (dmg >= hp) 
        return true;
    return false;
}

void solve(int n, ll hp) {
    vector<ll> res;

    ll l = 0;
    ll r = hp;

    while (l < r) {
        ll m = l+(r-l)/2;
        if (works(m, n, hp)) {
            r = m;
        } else {
            l = m+1;
        }
    }

    // out
    cout << l << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        ll hp;
        cin >> n >> hp;
        arr = rints(n);
        solve(n, hp);
    }

    return 0;
}
