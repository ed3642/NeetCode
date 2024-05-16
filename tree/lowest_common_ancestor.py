# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # post-order
        # propagate up if the children of each node have one of the nodes were searching
        # the first node with p and q as children is the LCA
        
        def dfs(node) -> 'TreeNode':
            if not node or node == p or node == q:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node
            else:
                return left or right # case where they are from the same tree and one of them gets left out
        
        return dfs(root)
        
