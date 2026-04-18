# https://leetcode.com/problems/recover-binary-search-tree

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # there will be exactly 2 nodes out of order in the inorder traversal
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        # 1,2,3,7,5,4
        # find them and swap them
        
        def dfs(node):
            nonlocal first, second, prev
            if not node:
                return None
            
            dfs(node.left)
            
            if prev and node.val < prev.val:
                if not first:
                    first = prev
                    second = node
                else:
                    second = node
            
            prev = node

            dfs(node.right)

        first = None
        second = None
        prev = None
        dfs(root)

        first.val, second.val = second.val, first.val


    def recoverTree(self, root: Optional[TreeNode]) -> None:

        # 1,2,3,7,5,4
        # find them and swap them
        
        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            order.append(node)
            dfs(node.right)

        order = []
        dfs(root)
        
        first = None
        second = None
        N = len(order)
        for i in range(N - 1):
            if order[i].val > order[i + 1].val:
                if not first:
                    first = order[i]
                    second = order[i + 1]
                else:
                    second = order[i + 1]
                    break
        
        first.val, second.val = second.val, first.val
