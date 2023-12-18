from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # dont know yet
        def inOrder(root):
            if not root: 
                return
            inOrder(root.left)
            order.append(root.val)
            inOrder(root.right)
        
        order = []
        inOrder(root)
        print(order)
        return 1