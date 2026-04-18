# https://leetcode.com/problems/minimum-absolute-difference-in-bst
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal min_diff, prev_val
            if not node:
                return None, None
            

            dfs(node.left)
            if prev_val != float('inf'):
                diff = node.val - prev_val
                min_diff = min(diff, min_diff)
            prev_val = node.val
            dfs(node.right)
        
        min_diff = float('inf')
        prev_val = float('inf')
        dfs(root)
        return min_diff