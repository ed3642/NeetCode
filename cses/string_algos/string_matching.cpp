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

void solve(string s, string pattern) {
    /*
    basic kmp
    */
    
    int n = s.size();
    int m = pattern.size();
    vi lps(m);
    int c = 0;

    int mtc = 0;
    for (int i = 1; i < m; i++) {
        while (mtc > 0 && pattern[i] != pattern[mtc])
            mtc = lps[mtc-1];
        if (pattern[mtc] == pattern[i])
            mtc++;
        lps[i] = mtc;
    }

    mtc = 0;
    for (int i = 0; i < n; i++) {
        while (mtc > 0 && s[i] != pattern[mtc]) 
            mtc = lps[mtc-1];
        if (pattern[mtc] == s[i])
            mtc++;
        if (mtc == m) {
            c++;
            mtc = lps[mtc-1]; // look for this block again
        }
    }

    cout << c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    cin >> s;
    string pattern;
    cin >> pattern;

    solve(s, pattern);

    return 0;
}
