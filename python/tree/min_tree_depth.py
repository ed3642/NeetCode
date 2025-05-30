# https://leetcode.com/problems/minimum-depth-of-binary-tree

from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        q = deque([root])
        depth = 1

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        
        return 0

    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, depth):
            if not node:
                return float('inf')
            if not node.left and not node.right:
                return depth
            
            left = dfs(node.left, depth + 1)
            right = dfs(node.right, depth + 1)

            return min(left, right)
        
        if not root:
            return 0

        return dfs(root, 1)