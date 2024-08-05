# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(l, r):
            if bool(l) ^ bool(r):
                return False
            if not l and not r:
                return True
            if l.val != r.val:
                return False
            
            left = dfs(l.right, r.left)
            right = dfs(l.left, r.right)
            if l.val == r.val and left and right:
                return True
            
        return dfs(root.left, root.right)