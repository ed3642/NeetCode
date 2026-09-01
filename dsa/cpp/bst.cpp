#include <bits/stdc++.h>
using namespace std;

class FenwickTree {
public:
    // sum fenwick tree
    // elems must be 0 indexed to create, other ops are 1 indexed
    FenwickTree(const vector<int>& elems) {
        n = (int)elems.size();
        tree.assign(n + 1, 0);

        for (int i = 0; i < n; i++) {
            tree[i + 1] = elems[i];
        }
        for (int i = 1; i <= n; i++) {
            int j = i + (i & -i);
            if (j <= n) {
                tree[j] += tree[i];
            }
        }
    }

    int query(int i) {
        int sum = 0;
        while (i > 0) {
            sum += tree[i];
            i -= i & -i;
        }
        return sum;
    }

    void update(int i, int delta) {
        while (i <= n) {
            tree[i] += delta;
            i += i & -i;
        }
    }

    // inclusive l and r
    int range_query(int l, int r) {
        return query(r) - query(l - 1);
    }

private:
    int n;
    vector<int> tree;
};