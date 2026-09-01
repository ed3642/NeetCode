#include <bits/stdc++.h>
using namespace std;

class SegTree {
    // associative range query in O(log n) with range updates and lazy propagation

public:
    SegTree(const vector<long long>& arr, long long default_val = 0) {
        n = (int)arr.size();
        default_ = default_val;
        size_ = 1;
        while (size_ < n) size_ <<= 1;

        tree.assign(2 * size_, default_);
        lazy.assign(2 * size_, 0);

        for (int i = 0; i < n; i++) {
            tree[size_ + i] = arr[i];
        }
        for (int i = size_ - 1; i >= 1; i--) {
            tree[i] = _merge(tree[2*i], tree[2*i+1]);
        }
    }

    /* Point update: kept for convenience, delegates to range_update. */
    void update(int idx, long long value) {
        range_update(idx, idx, value);
    }

    /* Range update: applies val to every element in [l, r]. */
    void range_update(int l, int r, long long val) {
        _update(1, 0, size_ - 1, l, r, val);
    }

    /* Range query on [l, r]. */
    long long query(int l, int r) {
        return _query(1, 0, size_ - 1, l, r);
    }

private:
    int n;
    int size_;
    long long default_;
    vector<long long> tree;
    vector<long long> lazy;

    long long _merge(long long left, long long right) {
        // sum:     return left + right;
        // min:     return min(left, right);
        // max:     return max(left, right);
        // gcd:     return __gcd(left, right);
        // product: return left * right;
        return left + right;
    }

    void _apply(int node, long long val, long long node_size) {
        // --- range ADD ---
        // sum query: tree stores segment total, so adding val shifts it by val * size
        tree[node] += val*node_size;
        // min/max query: the min/max shifts by val regardless of size
        // tree[node] += val;

        // --- range ASSIGN ---
        // sum query: every element becomes val, so total = val * size
        // tree[node] = val * node_size;
        // min/max query: the min/max of a constant range is just val
        // tree[node] = val;

        // always mirror the same operation onto lazy
        lazy[node] += val;    // for add
        // lazy[node] = val;  // for assign
    }

    void _push_down(int node, long long node_size) {
        if (lazy[node] != 0) {               // sentinel for add (no pending update)
        // if (lazy[node] has_value) {       // sentinel for assign (use e.g. LLONG_MIN or optional<long long> as "None")
            long long mid = node_size / 2;
            _apply(2*node, lazy[node], mid);
            _apply(2*node+1, lazy[node], node_size-mid);
            lazy[node] = 0;      // reset sentinel for add
            // lazy[node] = NONE_SENTINEL;  // reset sentinel for assign
        }
    }

    void _update(int node, int node_l, int node_r, int l, int r, long long val) {
        if (r < node_l || node_r < l) return;
        if (l <= node_l && node_r <= r) {
            _apply(node, val, node_r-node_l+1);
            return;
        }
        _push_down(node, node_r-node_l+1);
        int mid = (node_l + node_r) / 2;
        _update(2 * node, node_l, mid, l, r, val);
        _update(2 * node + 1, mid + 1, node_r, l, r, val);
        tree[node] = _merge(tree[2*node], tree[2*node+1]);
    }

    long long _query(int node, int node_l, int node_r, int l, int r) {
        if (r < node_l || node_r < l) return default_;
        if (l <= node_l && node_r <= r) return tree[node];
        _push_down(node, node_r - node_l + 1);
        int mid = (node_l + node_r) / 2;
        return _merge(
            _query(2 * node, node_l, mid, l, r),
            _query(2 * node + 1, mid + 1, node_r, l, r)
        );
    }
};