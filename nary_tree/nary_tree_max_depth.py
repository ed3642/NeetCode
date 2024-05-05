# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def dfs(node, depth):
            if not node:
                return None
            
            self.max_depth = max(self.max_depth, depth)
            for neighbor in node.children:
                dfs(neighbor, depth + 1)
        
        self.max_depth = 0
        dfs(root, 1)
        return self.max_depth