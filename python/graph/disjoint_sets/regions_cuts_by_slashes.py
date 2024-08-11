from collections import defaultdict

class UnionFind:
    def __init__(self, elements) -> None:
        self.parents = {e: e for e in elements}
        self.ranks = {e: 0 for e in elements}
        self.num_groups = len(elements)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.ranks[root_a] > self.ranks[root_b]:
                self.parents[root_b] = root_a
            elif self.ranks[root_a] < self.ranks[root_b]:
                self.parents[root_a] = root_b
            else:
                self.parents[root_b] = root_a
                self.ranks[root_a] += 1
            self.num_groups -= 1

    def connected(self, a, b):
        return self.find(a) == self.find(b)

class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:

        MAX_I = len(grid)
        MAX_J = len(grid[0])
        nodes = [(i, j, k) for i in range(MAX_I) for j in range(MAX_J) for k in range(1, 5)]
        ds = UnionFind(nodes)

        # Create nodes and store them in the adj_list
        for i in range(MAX_I):
            for j in range(MAX_J):
                left = (i, j, 1)
                top = (i, j, 2)
                right = (i, j, 3)
                bottom = (i, j, 4)

                if grid[i][j] == '/':
                    ds.union(left, top)
                    ds.union(right, bottom)
                elif grid[i][j] == '\\':
                    ds.union(left, bottom)
                    ds.union(right, top)
                else: # empty space
                    ds.union(left, top)
                    ds.union(top, right)
                    ds.union(right, bottom)

                # Connect to neighboring clusters
                if j > 0: # left neighbor
                    ds.union(left, (i, j - 1, 3))
                if i > 0: # top neighbor
                    ds.union(top, (i - 1, j, 4))

        return ds.num_groups
    
s = Solution()
print(s.regionsBySlashes([" /","/ "]))