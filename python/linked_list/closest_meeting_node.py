# https://leetcode.com/problems/find-closest-node-to-given-two-nodes

from collections import deque
from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # for this problem we can think of it as a jumbled linked list instead of a graph
        # since all nodes have max 1 out going 

        if node1 == node2:
            return node1
        
        N = len(edges)
        visited1 = [False] * N
        visited1[node1] = True
        visited2 = [False] * N
        visited2[node2] = True
        dist1 = [float('inf')] * N
        dist1[node1] = 0
        dist2 = [float('inf')] * N        
        dist2[node2] = 0

        # find distances from node1
        dist = 1
        while True:
            node1 = edges[node1]
            if node1 == -1 or visited1[node1]:
                break
            visited1[node1] = True
            dist1[node1] = dist
            dist += 1
        
        # find distances from node2 
        dist = 1
        while True:
            node2 = edges[node2]
            if node2 == -1 or visited2[node2]:
                break
            visited2[node2] = True
            dist2[node2] = dist
            dist += 1

        # find min(dist1[node] + dist2[node])

        best = float('inf')
        best_node = -1
        for node in range(N):
            cand = max(dist1[node], dist2[node])
            if cand < best:
                best = cand
                best_node = node
        
        return best_node
    