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

void solve(vi &arr, int n) {
    /*
    
    */
    
    ll c = 0;
    int mxSeen = arr[0];
    
    for (int i = 1; i < n; i++) {
        if (arr[i] < mxSeen) {
            c += (ll) mxSeen-arr[i];
        }
        mxSeen = max(mxSeen, arr[i]);
    }
    
    cout << c;
    // out
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vi arr = rvec<int>(n);
    solve(arr, n);

    return 0;
}
