# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0

        def dfs(root, depth):
            if not root:
                return
            self.max_depth = max(depth, self.max_depth)
            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)
        
        dfs(root, 1)
        return self.max_depth
    
    # iterative dfs
    def maxDepth_iter(self, root: Optional[TreeNode]) -> int:
        stack = deque([(root, 1)])
        max_depth = 0

        while stack:
            root, depth = stack.pop()
            if not root: continue
            max_depth = max(depth, max_depth)
            stack.append([root.left, depth + 1])
            stack.append([root.right, depth + 1])

        return max_depth