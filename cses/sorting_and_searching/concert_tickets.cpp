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

#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    // elems must be 0 indexed
    UnionFind(int size) {
        int n = size;
        parent.resize(n);
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    // dont want union by rank for the next pointer trick to work
    void unite(int a, int b) {
        int root_a = find(a);
        int root_b = find(b);
        parent[root_a] = root_b;
    }

    bool connected(int a, int b) {
        return find(a) == find(b);
    }

private:
    vector<int> parent;
};

void solve(vi &p, int n, vi &maxP, int m) {
    /* 
    solves with a next pointer trick with union find.
    This solution is about 2x faster than the set solution below.
    */
    sort(p.begin(), p.end());
    UnionFind uf(n+1); // make it 1 indexed so we can point next pointer to i-1

    for (int i = 0; i < m; i++) {
        auto it = upper_bound(p.begin(), p.end(), maxP[i]);
        if (it == p.begin()) {
            cout << -1 << '\n';
            continue;
        }
        it--;
        int index = it-p.begin();
        int nextOpen = uf.find(index+1); // +1 for 1-index
        if (nextOpen == 0 || nextOpen > n) {
            cout << -1 << '\n';
            continue;
        }
        cout << p[nextOpen-1] << '\n'; // -1 for 1-index
        uf.unite(nextOpen, nextOpen-1);
    }
}

void solve2(vi &p, int n, vi &maxP, int m) {
    /*
    solves with a multiset
    3 5 5 7 8
    4 8 3
    3 8 -1

    sets are a tree structure. not a sequence of memory so cant do it-begin()
    */
    
    multiset<int> pSet(p.begin(), p.end());

    for (int i = 0; i < m; i++) {
        auto it = pSet.upper_bound(maxP[i]);
         // 1 less than the first greater than value
        if (it == pSet.begin()) {
            cout << -1 << '\n';
            continue;
        }
        it--;
        cout << *it << '\n';
        pSet.erase(it);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    int m;
    cin >> n >> m;

    vi p = rvec<int>(n);
    vi maxP = rvec<int>(m);

    solve(p, n, maxP, m);

    return 0;
}
