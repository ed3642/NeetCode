# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, relation, streak):
            if not node:
                return
            
            self.longest_streak = max(self.longest_streak, streak)
            
            left_streak = streak + 1 if relation == 'R' else 1
            right_streak = streak + 1 if relation == 'L' else 1
            dfs(node.left, 'L', left_streak)
            dfs(node.right, 'R', right_streak)
        
        self.longest_streak = 0
        dfs(root, 'R', 0)
        return self.longest_streak