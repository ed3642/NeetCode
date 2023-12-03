
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        if not root: return []
        # dfs preorder
        self.children = [root.val]
        def dfs(root):
            if not root: return
            for child in root.children:
                self.children.append(child.val)
                dfs(child)
        dfs(root)
        return self.children
        