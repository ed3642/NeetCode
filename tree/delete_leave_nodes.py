from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def dfs(node):
            if not node:
                return
            
            if not node.left and not node.right and node.val == target:
                return True # signal to delete this
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and not right:
                node.left = None
            elif right and not left:
                node.right = None
            elif left and right:
                node.left = None
                node.right = None

            if not node.left and not node.right and node.val == target:
                return True # signal to delete this
        
        delete_root = dfs(root)
        if delete_root: 
            return None
        return root