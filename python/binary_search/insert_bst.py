# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if not node:
                continue

            if val <= node.val:
                if not node.left:
                    node.left = TreeNode(val)
                    break
                queue.append(node.left)
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    break
                queue.append(node.right)
                
        return root