# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # keep tract of longest path from left and right
    # post order traversal
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(root):
            if not root: 
                return 0
            left_length = dfs(root.left)
            right_length = dfs(root.right)
            combined_length = left_length + right_length
            self.max_diameter = max(combined_length, self.max_diameter)
            return max(left_length, right_length) + 1  
        
        dfs(root)
        return self.max_diameter