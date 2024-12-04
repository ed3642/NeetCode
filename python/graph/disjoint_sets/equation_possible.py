# https://leetcode.com/problems/satisfiability-of-equality-equations
from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(lambda: 0)

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        elif self.parent[x] != x:
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

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        # check all equal relations first then see if any of the not-equal relations are broken
        # represent equality be being in the same group
        
        # make graph representation of all equality relations
        uf = UnionFind()
        not_equality_relations = []
        for eq in equations:
            if eq[1] == '!':
                not_equality_relations.append(eq[0] + eq[3])
            else:
                uf.union(eq[0], eq[3])
        
        # check for contradictions
        for pair in not_equality_relations:
            root_a = uf.find(pair[0])
            root_b = uf.find(pair[1])
            if root_a == root_b:
                return False
        
        return True