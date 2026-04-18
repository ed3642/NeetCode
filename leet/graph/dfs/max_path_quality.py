# https://leetcode.com/problems/maximum-path-quality-of-a-graph/

from typing import List

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        
        def dfs(node: int, qua: int, t, visited_bitmask: int):
            nonlocal max_qua
            if t > maxTime:
                return 0
            if node == 0:
                max_qua = max(qua, max_qua)
            
            for nei, nei_t in adj_list[node]:
                cand_t = t + nei_t
                if cand_t <= maxTime:
                    cand_qua = qua
                    if not visited_bitmask & (1 << nei):
                        cand_qua += values[nei]
                    dfs(nei, cand_qua, cand_t, visited_bitmask | (1 << nei)) # activate this nei bit

        N = len(values)
        adj_list = [[] for _ in range(N)]

        for _from, _to, t in edges:
            adj_list[_from].append((_to, t))
            adj_list[_to].append((_from, t))

        max_qua = 0
        dfs(0, values[0], 0, 1)
        return max_qua
    