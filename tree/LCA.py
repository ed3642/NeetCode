# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # goes through entire tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # inorder traversal
        # LCA is in the middle of p and q in BST
        # question is basically asking for the number in the middle of two points in a binary search
        self.LCA = None

        def dfs(node):
            if not node: return
            if node.val > p.val and node.val > q.val:
                dfs(node.left)
            elif node.val < p.val and node.val < q.val:
                dfs(node.right)
            else:
                # this is LCA
                self.LCA = node
                return 
        
        dfs(root)
        return self.LCA 
    
    # stops right away
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.LCA = None

        def dfs(node):
            if not node or self.LCA:
                return
            if node.val > p.val and node.val > q.val:
                dfs(node.left)
            elif node.val < p.val and node.val < q.val:
                dfs(node.right)
            else:
                self.LCA = node

        dfs(root)
        return self.LCA