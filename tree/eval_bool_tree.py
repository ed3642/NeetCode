# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node.left and not node.right:
                if node.val == 0:
                    return False
                elif node.val == 1:
                    return True
            
            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == 2:
                return left or right
            elif node.val == 3:
                return left and right
        
        return dfs(root)