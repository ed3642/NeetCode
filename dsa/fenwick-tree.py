from typing import List

class FenwickTree:
    # sum fenwick tree
    # elems must be 0 indexed
    def __init__(self, elems: List[int]):
        self.n = len(elems)
        self.tree = [0] * (self.n+1)

        for i in range(self.n):
            self.tree[i+1] = elems[i]
        for i in range(1, self.n+1):
            j = i + (i & -i)
            if j <= self.n:
                self.tree[j] += self.tree[i]

    def query(self, i):
        sum = 0
        while i > 0:
            sum += self.tree[i]
            i -= i & -i
        return sum

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i
    
    # inclusive l and r
    def range_query(self, l, r):
        return self.query(r)  - self.query(l-1)