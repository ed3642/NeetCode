# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # goes through entire tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # traverse inorder and see if theres ever a node less than the prev one
        self.is_valid = True
        self.prev = None

        def dfs(root):
            if not root: return
            dfs(root.left)
            if self.prev and root.val <= self.prev.val:
                self.is_valid = False
                return
            self.prev = root
            dfs(root.right)
        
        dfs(root)
        return self.is_valid
    
    # stops right away
    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        self.prev = None

        def dfs(node):
            if not node:
                return True
            if not dfs(node.left):
                return False
            if self.prev and node.val <= self.prev.val:
                return False
            self.prev = node
            return dfs(node.right)

        return dfs(root)