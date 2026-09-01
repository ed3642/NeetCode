# https://leetcode.com/problems/remove-methods-from-project

from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        def dfs1(node):
            is_sus[node] = True

            for nei in g[node]:
                if not is_sus[nei]:
                    dfs1(nei)

        def dfs2(node):
            for nei in g[node]:
                if is_sus[nei]:
                    return True
            return False


        g = [[] for _ in range(n)]
        is_sus = [False] * n

        for f, t in invocations:
            g[f].append(t)

        dfs1(k)
        for node in range(n):
            if not is_sus[node]:
                calls_sus = dfs2(node)
                if calls_sus:
                    return [i for i in range(n)]

        res = []
        for i in range(n):
            if not is_sus[i]:
                res.append(i)

        return res