# https://leetcode.com/problems/binary-tree-maximum-path-sum

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal best
            if not node:
                return 0
            
            l = dfs(node.left)
            r = dfs(node.right)

            take_none = node.val
            take_one_side = max(l, r)+node.val
            take_both_sides = l+r+node.val
            node_best = max(take_none, take_one_side)
            best = max(node_best, take_both_sides, best)
            return node_best

        best = -float('inf')
        dfs(root)
        return best

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0
            
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            tree_sum = left + right + node.val

            best_split_sum = max(left, right) + node.val
            max_sum = max(best_split_sum, tree_sum, max_sum)
            return best_split_sum

        max_sum = -float('inf')
        dfs(root)
        return max_sum