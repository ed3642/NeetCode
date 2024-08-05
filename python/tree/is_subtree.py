# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.is_subtree = False

        def isSameTree(root1, root2):
            if not root1 and not root2:
                return True
            if (not root1) ^ (not root2):
                return False
            if root1.val != root2.val:
                return False
            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        def dfs(root):
            if not root: return
            if self.is_subtree: return
            self.is_subtree = isSameTree(root, subRoot)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return self.is_subtree

