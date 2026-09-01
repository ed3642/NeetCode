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
const ll MOD = 1e9+7;
const ll INF = LLONG_MAX;

inline vi rints(int n) { vi v(n); for (int &x : v) cin >> x; return v; }
inline vc rchars(int n) { vc v(n); for (char &c : v) cin >> c; return v; }
inline string rstring() { string s; cin >> s; return s; }
inline vs rall() { vs v; for (string s; cin >> s; ) v.push_back(s); return v; }
inline int vMin(const vi& v) { return *min_element(v.begin(), v.end()); }
inline int vMax(const vi& v) { return *max_element(v.begin(), v.end()); }

void solve(int n, int k) {
    /*
    in this problem k is always 3
    */
    
    if (n % 2 != 0) {
        int a = (n-1)/2;
        cout << a << ' ' << a << ' ' << 1 << '\n';
    } else {
        int a = (n-2)/2; // assume c = 2
        int c = (a % 2 == 0) ? 2 : n/2;
        a = (n-c)/2; // recalculate 'a' with c=n/2 if c=2 makes 'a' odd

        cout << a << ' ' << a << ' ' << c << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        int k;
        cin >> n >> k;
        solve(n, k);
    }

    return 0;
}
