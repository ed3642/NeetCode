
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    # return True when all nodes are connected
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

    def areConnected(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        # return last unadded edge

        n = len(edges)
        ds = UnionFind(n)

        for i in range(n):
            a, b = edges[i]
            if ds.areConnected(a - 1, b - 1):
                return [a, b]
            ds.union(a - 1, b - 1)
        
        return []
