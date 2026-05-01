# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations

from collections import Counter, defaultdict
from typing import List

class UnionFind:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

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
            elif self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            else:
                self.parent[root_a] = root_b
                self.rank[root_b] += 1
    
    def joined(self, a, b):
        return self.find(a) == self.find(b)

class Solution:

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        n = len(source)
        uf = UnionFind(n)
        counts = defaultdict(Counter)

        for i, j in allowedSwaps:
            uf.union(i, j)
        
        for i in range(n):
            root = uf.find(i)
            counts[root][source[i]] += 1
        
        misses = 0
        for i in range(n):
            root = uf.find(i)
            if counts[root][target[i]] == 0:
                misses += 1
            else:
                # swap this elem here
                counts[root][target[i]] -= 1

        return misses

class UnionFind:
    # keep track of whats in each group
    # solution could be better. This solution merges the counts on each union we can just count the elems at the end once after all union like on the above solution
    
    def __init__(self, n, arr):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.arr = arr
        self.counts = defaultdict(Counter)

        for i in range(n):
            self.counts[i] = Counter([arr[i]])
    
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
                self.merge_counts(root_b, root_a)
            elif self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
                self.merge_counts(root_a, root_b)
            else:
                self.parent[root_a] = root_b
                self.rank[root_b] += 1
                self.merge_counts(root_b, root_a)

    def merge_counts(self, new_root, other_root):
        self.counts[new_root].update(self.counts[other_root])
        del self.counts[other_root]
    
    def joined(self, a, b):
        return self.find(a) == self.find(b)

class Solution:

    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        n = len(source)
        
        uf = UnionFind(n, source)

        for i, j in allowedSwaps:
            uf.union(i, j)
        
        misses = 0
        for i in range(n):
            root = uf.find(i)
            if uf.counts[root][target[i]] == 0:
                misses += 1
            else:
                # swap this elem here
                uf.counts[root][target[i]] -= 1

        return misses