class UnionFind:
    def __init__(self, elements):
        self.parent = {element: element for element in elements}
        self.rank = {element: 0 for element in elements}
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # path compression
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        # union by rank
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            else:
                self.parent[root_b] = root_a
                self.rank[root_a] += 1
    
    def parents_count(self):
        return sum(i == parent for i, parent in self.parent.items())

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        disjoint_sets = UnionFind([i for i in range(n)])

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    disjoint_sets.union(i,j)
        
        return disjoint_sets.parents_count()
