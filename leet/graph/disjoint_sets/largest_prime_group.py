# https://leetcode.com/problems/largest-component-size-by-common-factor/

from typing import List

class UnionFind:
    def __init__(self, elems):
        self.parent = {e: e for e in range(len(elems))}
        self.rank = {e: 0 for e in range(len(elems))}
        self.size = {e: 1 for e in range(len(elems))}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            if self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
                self.size[root_b] += self.size[root_a]
            elif self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
                self.size[root_a] += self.size[root_b]
            else:
                self.parent[root_a] = root_b
                self.rank[root_b] += 1
                self.size[root_b] += self.size[root_a]
    
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:

        def prime_factors(x):
            factors = set()
            d = 2
            while d * d <= x:
                if x % d == 0:
                    factors.add(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                factors.add(x)
            return factors

        uf = UnionFind(nums)
        prime_to_index = {}

        for i, num in enumerate(nums):
            for p in prime_factors(num):
                if p in prime_to_index:
                    uf.union(i, prime_to_index[p])
                prime_to_index[p] = i

        return max(uf.size.values())