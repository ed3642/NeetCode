class SegTree:
    # associative range query in O(log n)

    def __init__(self, arr, default=0):
        """
        arr: initial array
        default: identity value of the operation
                 sum  -> 0
                 min  -> +inf
                 max  -> -inf
                 gcd  -> 0
                 ...
        """
        self.n = len(arr)
        self.default = default
        self.size = 1
        while self.size < self.n:
            self.size <<= 1

        # allocate tree
        self.tree = [default] * (2 * self.size)

        # build leaves
        for i in range(self.n):
            self.tree[self.size + i] = arr[i]

        # build internal nodes
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = self._merge(self.tree[2*i], self.tree[2*i + 1])

    # Problem specific func, prob need to change per problem
    def _merge(self, left, right):
        """
        Defines how two segments combine.
        Change this depending on the problem:
            sum: return left + right
            min: return min(left, right)
            max: return max(left, right)
            gcd: return math.gcd(left, right)
            ...
        """
        return left + right

    def update(self, idx, value):
        """
        Point update: arr[idx] = value
        """
        pos = self.size + idx
        self.tree[pos] = value

        # re-calc parents
        pos //= 2
        while pos >= 1:
            self.tree[pos] = self._merge(self.tree[2*pos], self.tree[2*pos + 1])
            pos //= 2

    def query(self, l, r):
        """
        Range query on interval [l, r]
        """
        l += self.size
        r += self.size
        res = self.default

        while l <= r:
            if l & 1:
                res = self._merge(res, self.tree[l])
                l += 1
            if not (r & 1):
                res = self._merge(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2

        return res
