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

void solve(vi arr, int n, int x) {

    /*
    if x | sum => subtracting a number y so that (x !| y)
    will make sum-y % x != 0
    since y % x != 0;
    */

    int sum = 0;
    for (int i = 0; i < n; i++) 
        sum += arr[i];

    int firstNonDivI = -1;
    int lastNonDivI = -1;

    for (int i = 0; i < n; i++) {
        if (arr[i] % x != 0) {
            firstNonDivI = i;
            break;
        }
    }
    for (int i = n-1; i > -1; i--) {
        if (arr[i] % x != 0) {
            lastNonDivI = i;
            break;
        }
    }

    // out
    if (sum % x != 0) {
        cout << n << '\n';
    } else if (firstNonDivI != -1) {
        if (firstNonDivI+1 < n-lastNonDivI)
            cout << n-(firstNonDivI+1) << '\n';
        else
            cout << lastNonDivI << '\n';
    } else {
        cout << -1 << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        int x;
        cin >> n >> x;

        solve(rints(n), n, x);
    }

    return 0;
}
