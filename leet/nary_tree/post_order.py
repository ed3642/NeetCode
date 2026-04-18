# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if not root: return []
        # dfs preorder
        self.children = []
        def dfs(root):
            if not root: return
            for child in root.children:
                dfs(child)
                self.children.append(child.val)
        dfs(root)
        self.children.append(root.val)
        return self.children
        