# https://leetcode.com/problems/most-profitable-path-in-a-tree
from collections import defaultdict, deque
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        # iff path between alice and bob is odd there is 1 node where they collide (middle one)

        def dfs(node, visited):
            if visited[node]:
                return 0
            visited[node] = True
            
            max_sum = -float('inf')
            if node != 0 and len(adj_list[node]) == 1: # is leaf
                return max(amount[node], max_sum)
            
            for nei in adj_list[node]:
                if not visited[nei]:
                    max_sum = max(dfs(nei, visited) + amount[node], max_sum) 
            
            return max_sum 
        
        def bob_bfs(node):
            
            q = deque([node])

            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if node == 0:
                        return
                    for nei in adj_list[node]:
                        if nei not in parent:
                            parent[nei] = node
                            q.append(nei)

        adj_list = defaultdict(list)
        adj_list[0] = []

        for _from, _to in edges:
            adj_list[_from].append(_to)
            adj_list[_to].append(_from)

        parent = {}
        bob_bfs(bob)
        # build alice bob path
        alice_bob_path = []
        node = 0
        while node != bob:
            alice_bob_path.append(node)
            if node not in parent: break
            node = parent[node]
        alice_bob_path.append(bob)

        # update val of nodes after they collide
        collide_node = len(alice_bob_path) // 2
        collide_node_val = amount[alice_bob_path[collide_node]]
        for node in alice_bob_path[collide_node:]:
            amount[node] = 0
        if len(alice_bob_path) % 2 != 0: # headon collision here
            amount[alice_bob_path[collide_node]] = collide_node_val // 2

        return dfs(0, [False] * len(amount))
    