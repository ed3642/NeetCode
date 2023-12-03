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