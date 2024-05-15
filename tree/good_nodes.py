# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # inorder
        # check if path is always inc
        self.count = 0

        def dfs(root, largest):
            if not root: return
            # process
            if root.val >= largest:
                self.count += 1
            if root.left:
                dfs(root.left, max(root.left.val, largest))
            if root.right:
                dfs(root.right, max(root.right.val, largest))
        
        dfs(root, root.val)
        return self.count
    
    def goodNodes2(self, root: TreeNode) -> int:
        
        def dfs(node, max_path_val):
            if not node:
                return
            new_max = max_path_val
            if max_path_val <= node.val:
                new_max = node.val
                self.count += 1
            dfs(node.left, new_max)
            dfs(node.right, new_max)
        
        self.count = 0
        dfs(root, -float('inf'))
        return self.count