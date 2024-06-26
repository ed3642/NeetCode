# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if (not root1) ^ (not root2):
                return False
            if root1.val != root2.val:
                return False
            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
        
        return dfs(p, q)
    
    def isSameTreeIterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque([(p, q)])
        
        while queue:
            p, q = queue.popleft()
            if bool(p) ^ bool(q): 
                return False
            if not p and not q:
                continue
            if not p.val == q.val:
                return False
            queue.append((p.left, q.left))
            queue.append((p.right, q.right))
        return True
