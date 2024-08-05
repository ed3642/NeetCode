# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # bfs 
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        levels = []
        stack = deque([root])

        while stack:
            level = []
            for _ in range(len(stack)):
                node = stack.popleft()
                if not node: continue
                level.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
            if len(level) > 0:
                levels.append(level)
        
        return levels
