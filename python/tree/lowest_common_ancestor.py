# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
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
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            nonlocal lca
            if not node:
                return 0
            if lca:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            found = left + right
            if node.val == p.val or node.val == q.val:
                found += 1

            if found == 2:
                lca = node # found
                return 0
            
            return found

        lca = None
        dfs(root)
        return lca
        
