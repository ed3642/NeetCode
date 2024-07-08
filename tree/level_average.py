# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        
        queue = deque([root])
        res = []
        while queue:
            level_sum = 0
            level_length = len(queue)
            for _ in range(level_length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_sum += node.val
            res.append(level_sum / level_length)
        return res