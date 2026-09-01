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

void solve(vi &aps, int n, vi &req, int m, int k) {
    /*
    sort both arrays and match each applicant to the minimum sized appartment available.
    if the next available appartment is too big, no available appartment exists for that applicant
    */
    
    sort(aps.begin(), aps.end());
    sort(req.begin(), req.end());

    int i = 0;
    int j = 0;
    int c = 0;

    while (i < n && j < m) {
        if (aps[i]-k > req[j]) { // ap too big, see if next guy wants it
            j++;
        } else if (aps[i]+k < req[j]) { // ap too small, no one will want it
            i++;
        } else { // ith ap suites jth person
            c++;
            i++;
            j++;
        }
    }

    cout << c;
    // out
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int m;
    int k;
    cin >> n >> m >> k;

    vi aps = rvec<int>(n);
    vi req = rvec<int>(m);

    solve(aps, n, req, m, k);

    return 0;
}
