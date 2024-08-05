# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node: 
                return
            
            if val < node.val:
                return dfs(node.left)
            elif val > node.val:
                return dfs(node.right)
            else:
                return node
        
        return dfs(root)
