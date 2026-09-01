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
 
void solve(int n) {
    /*
    if num pairs != odd to make n or (n-1) is not even
    then we cant split the seq into even sums.
 
    if n is odd, split by forming pairs that sum to n.
    if n is even, split by making pairs of (n+1).
    */
    
    if (n % 2 == 0) {
        int numPairs = n/2;
        if (numPairs % 2 == 1) {
            cout << "NO";
            return;
        }
 
        int groupSz = numPairs/2;
        cout << "YES" << '\n';
        
        cout << numPairs << '\n';
        int num = 1;
        for (int i = 0; i < groupSz; i++) {
            cout << num << ' ' << (n+1)-num << ' ';
            num++;
        }
        cout << '\n';
 
        cout << numPairs << '\n';
        for (int i = 0; i < groupSz; i++) {
            cout << num << ' ' << (n+1)-num << ' ';
            num++;
        }
 
    } else {
        int numsForPairs = (n-1);
        if (numsForPairs % 2 == 1) {
            cout << "NO";
            return;
        }
        int pairs = numsForPairs/2;
        if (pairs % 2 == 0) {
            cout << "NO";
            return;
        }
    
        cout << "YES" << '\n';
        int group1Sz = pairs/2; // group with the nth num in it
        int group2Sz = pairs-group1Sz;
    
        cout << group1Sz*2+1 << '\n'; // +1 to include the manually placed n
        int num = 1;
        for (int i = 0; i < group1Sz; i++) {
            cout << num << ' ' << (n-num) << ' ';
            num++;
        }
        cout << n;
        cout << '\n';
    
        cout << group2Sz*2 << '\n';
        for (int i = 0; i < group2Sz; i++) {
            cout << num << ' ' << (n-num) << ' ';
            num++;
        }
    }
    
}
 
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int n;
    cin >> n;
 
    solve(n);
 
    return 0;
}