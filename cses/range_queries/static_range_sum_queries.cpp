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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int q;
    cin >> n >> q;

    vi arr = rvec<int>(n);
    vll pf(n+1);
    for (int i = 0; i < n; i++)
        pf[i+1] = arr[i];
    for (int i = 2; i <= n; i++)
        pf[i] += (ll) pf[i-1];

    for (int _ = 0; _ < q; _++) {
        int l;
        int r;
        cin >> l >> r;
        cout << (ll) pf[r]-pf[l-1] << '\n';
    }

    return 0;
}
