# https://leetcode.com/problems/path-with-maximum-probability/
from collections import deque

class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        # SPFA but for longest path
        
        adj_list = [[] for _ in range(n)]
        for i, (_from, _to) in enumerate(edges):
            adj_list[_from].append((_to, succProb[i]))
            adj_list[_to].append((_from, succProb[i]))

        probs = [0] * n
        probs[start_node] = 1
        q = deque([(1, start_node)]) # prob, node

        while q:
            prob, node = q.popleft()
            
            for nei_node, nei_prob in adj_list[node]:
                cand_prob = prob * nei_prob
                if cand_prob > probs[nei_node]:
                    q.append((cand_prob, nei_node))
                    probs[nei_node] = cand_prob

        return probs[end_node]
