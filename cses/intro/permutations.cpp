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

void solve(int n) {
    /*
    1 2 3 4 5 
    1 4 2 5 3

    1 2 3 4
    2 4 1 3

    1 2 3 4 5 6
    1 4 2 5 3 6

    separate the small nums with a big num.
    Only hard to work with n<4
    */

    if (n == 1) {
        cout << 1;
        return;
    }
    else if (n <= 3) {
        cout << "NO SOLUTION";
        return;
    } else if (n == 4) { // its late just do this
        cout << 2 << ' ' << 4 << ' ' << 1 << ' ' << 3;
        return;
    }
    
    vi order(n);

    int num = 1;
    for (int i = 0; i < n; i += 2) {
        order[i] = num;
        num++;
    }
    for (int i = 1; i < n; i += 2) {
        order[i] = num;
        num++;
    }

    for (int i = 0; i < n; i++) {
        cout << order[i] << ' ';
    }
    return;
    // out
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    solve(n);

    return 0;
}
