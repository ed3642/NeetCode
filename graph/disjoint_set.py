# fast union
class UnionFind:
    def __init__(self, elements):
        self.parent = {element: element for element in elements}
        self.rank = {element: 0 for element in elements}

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # path compression
        return self.parent[x]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        # union by rank
        if parent_a != parent_b:
            if self.rank[parent_a] > self.rank[parent_b]:
                self.parent[parent_b] = parent_a
            elif self.rank[parent_a] < self.rank[parent_b]:
                self.parent[parent_a] = parent_b
            else:
                self.parent[parent_b] = parent_a
                self.rank[parent_a] += 1

    def connected(self, a, b):
        return self.find(a) == self.find(b)