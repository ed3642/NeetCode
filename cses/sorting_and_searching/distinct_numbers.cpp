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

void solve(vi &arr, int n) {
    /*
    interesting c++ feature from this problem.
    reserving space for a hashing structure avoids having to rehash
    making this solution 10x faster by reserving the space.

    reserve n*2 space to avoid reshaing as much as possible, n would work too but might have to rehash more times.

    You could also solve this by sorting the arr and seeing how many times arr[i] != arr[i-1]
    */

    unordered_set<int> setA;
    setA.reserve(n*2); // avoid rehashing

    setA.insert(arr.begin(), arr.end());

    cout << setA.size();
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
