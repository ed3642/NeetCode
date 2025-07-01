# https://leetcode.com/problems/lexicographically-smallest-equivalent-string

class UnionFind:
    def __init__(self, elems):
        self.parent = {e: e for e in elems}
        self.rank = {e: 0 for e in elems}
        self.smallest_from_group = {e: e for e in elems}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)


        if root_a != root_b:
            # set the best
            sm_a = self.smallest_from_group[root_a]
            sm_b = self.smallest_from_group[root_b]
            if sm_a < sm_b:
                self.smallest_from_group[root_a] = sm_a
                self.smallest_from_group[root_b] = sm_a
            else:
                self.smallest_from_group[root_a] = sm_b
                self.smallest_from_group[root_b] = sm_b
            # update the rank
            if self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            elif self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            else:
                self.rank[root_a] += 1
                self.parent[root_b] = root_a

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        uf = UnionFind(alphabet)

        for i in range(len(s1)):
            uf.union(s1[i], s2[i])
        
        n = len(baseStr)
        res = [''] * n
        for i in range(n):
            root = uf.find(baseStr[i])
            res[i] = uf.smallest_from_group[root]
        
        return ''.join(res)