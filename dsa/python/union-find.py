from typing import List

class UnionFind:
    # elems must be 0 indexed
    def __init__(self, elems: List[int]):
        self.parent = [i for i in range(len(elems))]
        self.rank = [0 for _ in range(len(elems))]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            else:
                self.parent[root_a] = root_b
                self.rank[root_b] += 1