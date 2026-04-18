# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node, depth):
            if not node:
                return [-1, -1]
            if not node.left and not node.right:
                return [node, depth]
            
            left = [-1, -1]
            right = [-1, -1]
            if node.left:
                left = dfs(node.left, depth + 1)
            if node.right:
                right = dfs(node.right, depth + 1)

            if left[1] > right[1]:
                return left
            elif left[1] < right[1]:
                return right
            return [node, left[1]]
        
        return dfs(root, 0)[0]
