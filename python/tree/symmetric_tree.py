# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(left_child, right_child):
            if bool(left_child) ^ bool(right_child):
                return False
            if not left_child and not right_child:
                return True
            if left_child.val != right_child.val:
                return False
            
            res_1 = dfs(left_child.left, right_child.right)
            res_2 = dfs(left_child.right, right_child.left)
            return res_1 and res_2


        return dfs(root.left, root.right)