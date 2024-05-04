import heapq

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.groups = n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.groups -= 1
            if self.rank[root_a] < self.rank[root_b]:
                self.parent[root_a] = root_b
            elif self.rank[root_a] > self.rank[root_b]:
                self.parent[root_b] = root_a
            else:
                self.parent[root_a] = root_b
                self.rank[root_b] += 1
    
    def are_connected(self, a, b):
        return self.find(a) == self.find(b)

class Solution:
    # the key was to represent the nodes val (building that well) as
    # a dummy node with the nodes val as its weight
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
        # Kruskals MST

        heap = []
        ds = DisjointSet(n + 1)
        total_cost = 0

        # represent building a well as a dummy node
        # the problem is just a MST now
        for i, cost in enumerate(wells):
            heapq.heappush(heap, (cost, 0, i + 1)) # 0 represents the dummy node connecting to the well
        
        # add the other edges
        for _from, to, cost in pipes:
            heapq.heappush(heap, (cost, _from, to))
        
        while heap and ds.groups > 1:
            cost, _from, to = heapq.heappop(heap)

            if not ds.are_connected(_from, to):
                ds.union(_from, to)
                total_cost += cost
        
        return total_cost

