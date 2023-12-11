class DisjointSets:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.group_count = n
    
    def find(self, x):
        if x != self.parent[x]:
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
                self.parent[root_b] = root_a
                self.rank[root_a] += 1
            self.group_count -= 1
    
class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        ds = DisjointSets(n)
        for v1, v2 in edges:
            ds.union(v1, v2)
        
        return ds.group_count