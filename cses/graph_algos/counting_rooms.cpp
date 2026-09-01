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

vector<pii> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

int n;
int m;
vector<vector<char>> grid;

bool isIn(int i, int j) {
    return 0 <= i && i < n && 0 <= j && j < m;
}

void dfs(int i, int j) {
    grid[i][j] = '#';

    for (auto [di, dj] : directions) {
        int ni = i+di;
        int nj = j+dj;
        if (isIn(ni, nj) && grid[ni][nj] == '.') {
            dfs(ni, nj);
        }
    }
}

void solve() {
    
    int c = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (grid[i][j] == '.') {
                dfs(i, j);
                c++;
            }
        }
    }
    
    cout << c;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;

    grid.assign(n, vc(m));
    for (int i = 0; i < n; i++) {
        string row;
        cin >> row;
        vc rowVec(row.begin(), row.end());
        grid[i] = rowVec;
    }

    solve();

    return 0;
}
