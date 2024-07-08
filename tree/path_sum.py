# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, _sum):
            if not node:
                return False
            if _sum == targetSum and not node.left and not node.right:
                return True
            
            left = False
            right = False
            if node.left:
                left = dfs(node.left, _sum + node.left.val)
            if node.right:
                right = dfs(node.right, _sum + node.right.val)
            return left or right
        
        if root:
            return dfs(root, root.val)
        return False