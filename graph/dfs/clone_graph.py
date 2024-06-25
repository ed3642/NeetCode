from collections import defaultdict
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # better
    def cloneGraph2(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        def dfs(node):
            if node in visited:
                return visited[node]

            clone = Node(node.val)
            visited[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        
        visited = {}
        return dfs(node)

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None

        def dfs(node):
            if node not in visited:
                visited.add(node)
            else:
                return
            hm_nodes[node] = Node(node.val)
            for neighbor in node.neighbors:
                dfs(neighbor)

        visited = set() 
        hm_nodes = {}
        dfs(node) # copy values

        # copy edges
        for old_node, new_node in hm_nodes.items():
            for neighbor in old_node.neighbors:
                new_node.neighbors.append(hm_nodes[neighbor])
        
        return hm_nodes[node]
