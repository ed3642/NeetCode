# https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/
class DisjointSet:
    def __init__(self, n):
        self.parent = {node: node for node in range(1, n + 1)}
        self.rank = {node: 0 for node in range(1, n + 1)}
        self.groups = n

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
            self.groups -= 1

    def are_connected(self, a, b):
        return self.find(a) == self.find(b)
    
    def all_connected(self):
        return self.groups == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        # disjoint set, add edges only if they make a connection to a new node
        # do this for alice and bob and return the min
        # use type 3 edges first
        # processing type3 edges in a seperate loop makes us save some condition checking

        edges.sort(key=lambda x: -x[0])

        ds1 = DisjointSet(n)
        ds2 = DisjointSet(n)
        edges_used = 0
        num_edges = len(edges)
        i = 0

        # process type 3
        while i < num_edges:
            v_type, v1, v2 = edges[i]
            if v_type != 3:
                break
            if not ds1.are_connected(v1, v2):
                ds1.union(v1, v2)
                ds2.union(v1, v2)
                edges_used += 1
            i += 1

        # process types 1 and 2
        while i < num_edges:
            v_type, v1, v2 = edges[i]
            if v_type == 2 and not ds2.are_connected(v1, v2):
                ds2.union(v1, v2)
                edges_used += 1
            elif v_type == 1 and not ds1.are_connected(v1, v2):
                ds1.union(v1, v2)
                edges_used += 1
            if ds1.all_connected() and ds2.all_connected():
                break
            i += 1
        
        res = num_edges - edges_used
        return res if (ds1.all_connected() and ds2.all_connected()) else -1
