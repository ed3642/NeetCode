# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # post-order
        # keep track of the excess and defecit of each node, this is how many total moves we will need to make
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            self.moves += abs(left) + abs(right)

            return node.val + left + right - 1
        
        self.moves = 0
        dfs(root)
        return self.moves