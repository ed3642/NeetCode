# https://leetcode.com/problems/house-robber-iii

# Definition for a binary tree node.
from typing import Optional

    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # tree dp but we dont need to store extra stuff since each node is only computed once
        
        def dfs(node):
            if not node:
                return 0
            
            l_take, l_skip = 0, 0
            r_take, r_skip = 0, 0
            if node.left:
                l_take, l_skip = dfs(node.left)
            if node.right:
                r_take, r_skip = dfs(node.right)

            return (node.val+l_skip+r_skip, max(l_take, l_skip)+max(r_take, r_skip))

        rob_root, skip_root = dfs(root)
        return max(rob_root, skip_root)