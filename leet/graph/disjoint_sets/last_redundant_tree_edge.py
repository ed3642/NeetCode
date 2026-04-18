# https://leetcode.com/problems/redundant-connection/
from typing import List

class UnionFind:
    def __init__(self, N):
        self.parent = [node for node in range(N)]
        self.rank = [0] * N

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
    
    def are_connected(self, a, b):
        return self.find(a) == self.find(b)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # union find, see which edges are already connected before joining
        
        N = len(edges)
        last_redundant_edge = [-1, -1] # there should always be one edge to replace this in the problem def

        uf = UnionFind(N + 1)
        
        for a, b in edges:
            if uf.are_connected(a, b):
                last_redundant_edge = [a, b]
            uf.union(a, b)
            
        return last_redundant_edge 