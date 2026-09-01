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

void solve(vvi mt, int n, int m) {
    /* 
        1 1 3 4
    dx    0 2 1
    mul   3 4 3

    1 2 3 4 5 6 ... n
        i j
    
    gap made by (i, j) where i = j-1
    i => has i choices
    j => has n-i choices
    so the gap (i, j) composes i*(n-i) gaps

    good problem
    */

   if (n == 1) {
        cout << 0 << '\n';
        return;
   }
    
    ll res = 0;

    int k = n-1;
    vll mult(n-1);
    for (int i = 1; i <= k; i++) {
        mult[i-1] = (ll) i*(n-i);
    }

    for (int j = 0; j < m; j++) {
        vi arr(n);
        for (int i = 0; i < n; i++) {
            arr[i] = mt[i][j];
        }
        sort(arr.begin(), arr.end());

        for (int i = 1; i < n; i++) {
            res += (arr[i]-arr[i-1])*mult[i-1];
        }
    }
    
    // out
    cout << res << '\n';
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

        vvi matrix; 
        for (int _ = 0; _ < n; _++) {
            matrix.push_back(rints(m));
        }
        solve(matrix, n, m);
    }

    return 0;
}
