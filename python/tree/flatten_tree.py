# https://leetcode.com/problems/flatten-binary-tree-to-linked-list
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    # O(1) space but still with recursive stack, could do true O(1) with morris traversal
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node):
            nonlocal prev
            if not node:
                return
            
            dfs(node.right)
            dfs(node.left)

            node.right = prev
            node.left = None

            prev = node

        prev = None
        dfs(root)

    # O(n) space, but very simple
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(node):
            if not node:
                return
            order.append(node)
            dfs(node.left)
            dfs(node.right)

        order = []
        dfs(root)

        for i in range(len(order) - 1):
            node = order[i]
            node.left = None
            node.right = order[i + 1]

