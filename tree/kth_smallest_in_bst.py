# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []

        # inorder
        def dfs(root):
            if not root: return
            dfs(root.left)
            # process
            if len(order) == k:
                return
            order.append(root.val)
            dfs(root.right)

        dfs(root)
        return order[-1]