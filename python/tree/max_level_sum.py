# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([root])

        _max = -float('inf')
        max_level = 1
        level = 1
        while queue:
            _sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                _sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if _sum > _max:
                _max = _sum
                max_level = level
            level += 1

        return max_level
