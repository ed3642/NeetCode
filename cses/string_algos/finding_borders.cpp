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

void solve(string s) {
    /*
    lps and go to each border
    */
    
    int n = s.size();
    vi lps(n);

    int mtc = 0;
    for (int i = 1; i < n; i++) {
        while (mtc > 0 && s[i] != s[mtc])
            mtc = lps[mtc-1];
        if (s[mtc] == s[i])
            mtc++;
        lps[i] = mtc;
    }

    vi order;
    mtc = n;
    while (mtc > 0 && lps[mtc-1] > 0) {
        order.push_back(lps[mtc-1]);
        mtc = lps[mtc-1];
    }

    for (int i = (int) order.size()-1; i >= 0; i--)
        cout << order[i] << ' ';
    
    // out
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;

    solve(s);
    return 0;
}
