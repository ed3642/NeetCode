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

void solve(vi &arr, int n, int x) {
    /*
    9 8 8 9 10 8 5 8 7 10
    5 7 8 8 8 8 9 9 10 10
    */
    
    int r = n-1;
    int l = 0;
    int c = 0;

    sort(arr.begin(), arr.end());
    
    while (l <= r) {
        if (arr[l]+arr[r] > x) {
            r--;
        } else {
            l++;
            r--;
        }
        c++;
    }

    cout << c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int target;
    cin >> n >> target;

    vi arr = rvec<int>(n);
    solve(arr, n, target);

    return 0;
}
