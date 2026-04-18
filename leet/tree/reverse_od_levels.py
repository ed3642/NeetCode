# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree
from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # unique dfs traversal
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(left_node, right_node, state):
            if not left_node: # no need to check right since its a perfect tree
                return
            
            if state == 1:
                left_node.val, right_node.val = right_node.val, left_node.val
            dfs(left_node.left, right_node.right, state ^ 1)
            dfs(left_node.right, right_node.left, state ^ 1)
        
        dfs(root.left, root.right, 1)

        return root

    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # perfect binary tree, only swap the values
        # same as inverting a tree? no...

        def dfs(node, level):
            if not node:
                return
            
            if level % 2 != 0:
                odd_leveled_nodes[level].append(node)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        odd_leveled_nodes = defaultdict(list)
        dfs(root, 0)

        # reverse the values in each level
        for nodes in odd_leveled_nodes.values():
            n = len(nodes)
            for i in range(n // 2):
                nodes[i].val, nodes[n - 1 - i].val = nodes[n - 1 - i].val, nodes[i].val

        return root