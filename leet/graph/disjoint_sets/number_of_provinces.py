# https://leetcode.com/problems/number-of-provinces
from typing import List

class UnionFind:
    def __init__(self, num_elems):
        self.parent = [i for i in range(num_elems)]
        self.rank = [0 for _ in range(num_elems)]
        self.groups = num_elems

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
                self.parent[root_b] = root_a
                self.rank[root_a] += 1
            self.groups -= 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        N = len(isConnected)

        uf = UnionFind(N)

        for v1 in range(N):
            for v2 in range(N):
                if v1 != v2 and isConnected[v1][v2] == 1:
                    uf.union(v1, v2)
        
        return uf.groups