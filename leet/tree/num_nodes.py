# https://leetcode.com/problems/count-complete-tree-nodes

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    # O(log n)
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def get_depth(node, get_left):
            height = 0
            while node:
                if get_left:
                    node = node.left
                else:
                    node = node.right
                height += 1
            return height

        def dfs(node):
            if not node:
                return 0
            
            left_depth = get_depth(node, True)
            right_depth = get_depth(node, False)

            if left_depth == right_depth:
                return (1 << left_depth) - 1 # perfect full tree

            return dfs(node.left) + dfs(node.right) + 1
        
        if not root:
            return 0

        return dfs(root)

    # O(n)
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal count

            count += 1
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        if not root:
            return 0
        
        count = 0
        dfs(root)
        return count
