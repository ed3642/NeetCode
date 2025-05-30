class FenwickTree:
    # NOTE: fenwick trees can only handle operations that are invertible (+, -, *, /, XOR, etc)
    # for nonreversible operations use segment tree
    
    # 1 based indexing, 0th elem is ignored
    # inclusive ranges
    # useful for freq range queries with updates
    def __init__(self, size): # size is max(nums) + 1
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index, delta):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index # add the right most 1 bit

    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index # flip the right most 1 bit
        return total

    def range_query(self, start, end):
        return self.query(end) - self.query(start - 1)

    def less_than(self, value, max_index):
        return self.query(min(value - 1, max_index))

    def greater_than(self, value, max_index):
        return self.query(max_index) - self.query(min(value, max_index))