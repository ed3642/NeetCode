from collections import defaultdict

class DisjointSets:
    def __init__(self, n):
        self.parent = list(range(n))  # parent[i] is the parent of i
        self.rank = [0] * n

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

    def getGroups(self):
        groups = defaultdict(list)
        for i, parent in enumerate(self.parent):
            groups[self.find(parent)].append(i)
        return groups

# https://leetcode.com/problems/smallest-string-with-swaps/description/
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        res = list(s)
        n = len(s)
        ds = DisjointSets(n)
        for i1, i2 in pairs:  # union indexes
            ds.union(i1, i2)
        
        groups = ds.getGroups().values()
        for group in groups:
            group.sort()  # sort indexes
            chars = sorted(res[i] for i in group)  # sort characters
            for i, ch in zip(group, chars):
                res[i] = ch
            
        return ''.join(res)

s = Solution()
print(s.smallestStringWithSwaps("dcab", [[0,3],[1,2],[0,2]]))