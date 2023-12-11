class DisjointSets:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.groups_count = n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b) -> bool:
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
            self.groups_count -= 1
            if self.groups_count == 1:
                return True
        return False

class Solution:
    def earliestAcq(self, logs: list[list[int]], n: int) -> int:
        logs.sort()
        ds = DisjointSets(n)

        for ts, friend1, friend2 in logs:
            if ds.union(friend1, friend2):
                return ts
        
        return -1