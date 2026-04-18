# https://leetcode.com/problems/evaluate-division

from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def calc_val(_from, _to):
            q = deque([(_from, 1)])
            visited = set()

            while q:
                for _ in range(len(q)):
                    node, val = q.popleft()

                    for nei, mult in adj_list[node]:
                        if nei not in visited:
                            visited.add(nei)
                            if nei == _to:
                                return val * mult
                            q.append((nei, val * mult))
            return -1
        
        adj_list = defaultdict(list)

        for i, (v1, v2) in enumerate(equations):
            adj_list[v1].append((v2, values[i]))
            adj_list[v2].append((v1, 1 / values[i]))
        
        res = []

        for _from, _to in queries:
            if _from not in adj_list or _to not in adj_list:
                res.append(-1)
            elif _from == _to:
                res.append(1)
            else:
                res.append(calc_val(_from, _to))
            
        return res