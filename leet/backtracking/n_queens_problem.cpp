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

/*
interestingly vector scan is faster than hashing when the vector is small < 50 apparently. 
*/

class Solution {
ll ways;
int N;

void bt(int i, vi &cols, vi &diag1, vi &diag2) {
    if (i == N) {
        ways++;
        return;
    }

    for (int j = 0; j < N; j++) {
        if (cols[j] == 0) {
            int d1Key = i+j;
            int d2Key = i-j+N;
            if (diag1[d1Key] == 0 && diag2[d2Key] == 0) {
                // place a queen on this unattacked square
                cols[j] = 1;
                diag1[d1Key] = 1;
                diag2[d2Key] = 1;
                bt(i+1, cols, diag1, diag2);
                // remove it
                cols[j] = 0;
                diag1[d1Key] = 0;
                diag2[d2Key] = 0;
            }
        }
    }
}

public:
    int totalNQueens(int n) {
        ways = 0;
        N = n;
        vi rows(n, 0);
        vi cols(n, 0);
        vi diag1(n*2, 0); // top left to bot right
        vi diag2(n*2, 0); // bot left to top right

        bt(0, cols, diag1, diag2);

        return ways;
    }
};