#include <bits/stdc++.h>
using namespace std;

class UnionFind {
public:
    // elems must be 0 indexed
    UnionFind(int size) {
        int n = size;
        parent.resize(n);
        rank.assign(n, 0);
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

    void unite(int a, int b) {
        int root_a = find(a);
        int root_b = find(b);
        if (root_a != root_b) {
            if (rank[root_a] > rank[root_b]) {
                parent[root_b] = root_a;
            } else if (rank[root_a] < rank[root_b]) {
                parent[root_a] = root_b;
            } else {
                parent[root_a] = root_b;
                rank[root_b] += 1;
            }
        }
    }

    bool connected(int a, int b) {
        return find(a) == find(b);
    }

private:
    vector<int> parent;
    vector<int> rank;
};