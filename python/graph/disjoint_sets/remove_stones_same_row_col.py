# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column
from collections import defaultdict

class UnionFind:
    def __init__(self, elems):
        self.parents = {e : e for e in elems}
        self.ranks = {e : 0 for e in elems}
        self.group_count = len(elems)
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.group_count -= 1
            if self.ranks[root_a] < self.ranks[root_b]:
                self.parents[root_a] = root_b
            elif self.ranks[root_a] > self.ranks[root_b]:
                self.parents[root_b] = root_a
            else:
                self.parents[root_b] = root_a
                self.ranks[root_a] += 1

class Solution:
    def removeStones(self, stones: list[list[int]]) -> int:
        
        N = len(stones)
        rows = defaultdict(list)
        cols = defaultdict(list)
        MAX_POSSIBLE_COLS = 10 ** 4
        nodes = []

        for r, c in stones:
            node = r * MAX_POSSIBLE_COLS + c
            nodes.append(node)
            rows[r].append(node)
            cols[c].append(node)
        
        uf = UnionFind(nodes)

        for elems in rows.values():
            first = elems[0]
            for elem in elems[1:]:
                uf.union(first, elem)
        for elems in cols.values():
            first = elems[0]
            for elem in elems[1:]:
                uf.union(first, elem)
        
        return N - uf.group_count
        