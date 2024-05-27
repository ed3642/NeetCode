class FenwickTree:
    # 1 based indexing, 0th elem is ignored
    # inclusive ranges
    def __init__(self, size): # size is max(nums) + 1
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        while i <= self.size:
            self.tree[i] += delta
            i += i & -i

    def query(self, i):
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def range_query(self, i, j):
        return self.query(j) - self.query(i - 1)

    def less_than(self, x, i):
        return self.query(min(x - 1, i))

    def greater_than(self, x, i):
        return self.query(i) - self.query(min(x, i))