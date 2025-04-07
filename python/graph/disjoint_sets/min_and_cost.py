# https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph

from typing import List

class UnionFind:

    def __init__(self, size):
        self.parent = [node for node in range(size)]
        self.rank = [0 for _ in range(size)]
        self.cummulative = {} # overall & of a group by root node
    
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

    def connected(self, a, b):
        return self.find(a) == self.find(b)
        
    def add(self, node, weight):
        group_root = self.find(node)
        if group_root in self.cummulative:
            self.cummulative[group_root] &= weight
        else:
            self.cummulative[group_root] = weight

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        
        uf = UnionFind(n)

        for _from, _to, weight in edges:
            uf.union(_from, _to)
        # add weights once uf is fully built and settled
        for _from, _to, weight in edges:
            uf.add(_from, weight)
        
        res = [-1] * len(query)
        for i, (_from, _to) in enumerate(query):
            if uf.connected(_from, _to):
                res[i] = uf.cummulative[uf.find(_from)]
        
        return res