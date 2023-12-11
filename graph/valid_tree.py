class UnionFind:
    def __init__(self, elems):
        self.parent = {elem: elem for elem in elems}
        self.rank = {elem: 0 for elem in elems}
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    # modified to return false if a node is already in a set
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
        else:
            return False
        return True

    def root_count(self) -> int:
        return sum([1 if elem == self.parent[elem] else 0 for elem in self.parent])

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        disjoint_set = UnionFind([i for i in range(n)])

        # check no node is added twice into the same set
        for a, b in edges:
            if not disjoint_set.union(a, b):
                return False

        # check all nodes have the same root
        if disjoint_set.root_count() != 1:
            return False
        
        return True
