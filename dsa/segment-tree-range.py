class SegTree:
    # associative range query in O(log n) with range updates and lazy propagation

    def __init__(self, arr, default=0):
        self.n = len(arr)
        self.default = default
        self.size = 1
        while self.size < self.n:
            self.size <<= 1

        self.tree = [default] * (2 * self.size)
        self.lazy = [0] * (2 * self.size)

        for i in range(self.n):
            self.tree[self.size + i] = arr[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self._merge(self.tree[2*i], self.tree[2*i + 1])

    def _merge(self, left, right):
        # sum:     return left + right
        # min:     return min(left, right)
        # max:     return max(left, right)
        # gcd:     return math.gcd(left, right)
        # product: return left * right
        return left + right

    def _apply(self, node, val, node_size):
        # --- range ADD ---
        # sum query: tree stores segment total, so adding val shifts it by val * size
        self.tree[node] += val * node_size
        # min/max query: the min/max shifts by val regardless of size
        # self.tree[node] += val

        # --- range ASSIGN ---
        # sum query: every element becomes val, so total = val * size
        # self.tree[node] = val * node_size
        # min/max query: the min/max of a constant range is just val
        # self.tree[node] = val

        # always mirror the same operation onto lazy
        self.lazy[node] += val    # for add
        # self.lazy[node] = val   # for assign

    def _push_down(self, node, node_size):
        if self.lazy[node] != 0:          # sentinel for add (no pending update)
        # if self.lazy[node] is not None: # sentinel for assign (None = no pending update)
            mid = node_size // 2
            self._apply(2 * node,     self.lazy[node], mid)
            self._apply(2 * node + 1, self.lazy[node], node_size - mid)
            self.lazy[node] = 0     # reset sentinel for add
            # self.lazy[node] = None  # reset sentinel for assign

    def update(self, idx, value):
        """Point update: kept for convenience, delegates to range_update."""
        self.range_update(idx, idx, value)

    def range_update(self, l, r, val):
        """Range update: applies val to every element in [l, r]."""
        def _update(node, node_l, node_r):
            if r < node_l or node_r < l:
                return
            if l <= node_l and node_r <= r:
                self._apply(node, val, node_r - node_l + 1)
                return
            self._push_down(node, node_r - node_l + 1)
            mid = (node_l + node_r) // 2
            _update(2 * node,     node_l, mid)
            _update(2 * node + 1, mid + 1, node_r)
            self.tree[node] = self._merge(self.tree[2*node], self.tree[2*node+1])

        _update(1, 0, self.size - 1)

    def query(self, l, r):
        """Range query on [l, r]."""
        def _query(node, node_l, node_r):
            if r < node_l or node_r < l:
                return self.default
            if l <= node_l and node_r <= r:
                return self.tree[node]
            self._push_down(node, node_r - node_l + 1)
            mid = (node_l + node_r) // 2
            return self._merge(
                _query(2 * node,     node_l, mid),
                _query(2 * node + 1, mid + 1, node_r)
            )

        return _query(1, 0, self.size - 1)