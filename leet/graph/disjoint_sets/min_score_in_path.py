# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities

from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for _ in range(n+1)]
        self.min_edge = [float('inf') for _ in range(n+1)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b, w):
        root_a = self.find(a)
        root_b = self.find(b)
        new_group_min = min(self.min_edge[root_a], self.min_edge[root_b], w)
        if root_a != root_b:
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
                self.min_edge[root_a] = new_group_min
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
                self.min_edge[root_b] = new_group_min
            else:
                self.parent[root_a] = root_b
                self.rank[root_b] += 1
                self.min_edge[root_b] = new_group_min
        else:
            self.min_edge[root_a] = new_group_min

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        uf = UnionFind(n)

        for f, t, w in roads:
            uf.union(f, t, w)

        return uf.min_edge[uf.find(n)] # there is always a path by problem statement