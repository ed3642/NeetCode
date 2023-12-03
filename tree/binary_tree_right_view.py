# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        # bfs
        # return last node of each level
        q = deque([root])
        right_most_in_level = []

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if not node: continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            print(level)
            if len(level) > 0:
                right_most_in_level.append(level[-1])
        
        return right_most_in_level