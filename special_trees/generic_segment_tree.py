class SegmentTree:
    # generic segment tree implementation, range query like min, max, sum, xor ...
    def __init__(self, arr, function):
        self.n = len(arr)
        self.function = function
        self.tree = [0] * (4 * self.n)
        self.build_tree(arr, 0, self.n - 1, 0)

    def build_tree(self, arr, ss, se, si):
        if ss == se:
            self.tree[si] = arr[ss]
        else:
            mid = (ss + se) // 2
            self.build_tree(arr, ss, mid, 2 * si + 1)
            self.build_tree(arr, mid + 1, se, 2 * si + 2)
            self.tree[si] = self.function(self.tree[2 * si + 1], self.tree[2 * si + 2])

    def range_query(self, qs, qe):
        def query(ss, se, si):
            if ss > qe or se < qs:
                return None
            if qs <= ss and qe >= se:
                return self.tree[si]
            mid = (ss + se) // 2
            left = query(ss, mid, 2 * si + 1)
            right = query(mid + 1, se, 2 * si + 2)
            if left is None:
                return right
            if right is None:
                return left
            return self.function(left, right)
        return query(0, self.n - 1, 0)
    
    def update(self, i, value):
        def update_util(ss, se, si):
            if i < ss or i > se:
                return
            if ss == se:
                self.tree[si] = value
            else:
                mid = (ss + se) // 2
                update_util(ss, mid, 2 * si + 1)
                update_util(mid + 1, se, 2 * si + 2)
                self.tree[si] = self.function(self.tree[2 * si + 1], self.tree[2 * si + 2])
        update_util(0, self.n - 1, 0)