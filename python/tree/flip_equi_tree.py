# https://leetcode.com/problems/flip-equivalent-binary-trees/
from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if bool(node1) ^ bool(node2):
                return False
            if node1.val != node2.val:
                return False

            no_swap = dfs(node1.left, node2.left) and dfs(node1.right, node2.right)
            swap = dfs(node1.left, node2.right) and dfs(node1.right, node2.left)
            return no_swap or swap

        return dfs(root1, root2)

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node, children_dict):
            if not node: return

            if node.left:
                children_dict[node.val].add(node.left.val)
                dfs(node.left, children_dict)
            if node.right:
                children_dict[node.val].add(node.right.val)
                dfs(node.right, children_dict)

        children1 = defaultdict(set)
        children2 = defaultdict(set)
        if root1:
            children1[-1].add(root1.val)
        if root2:
            children2[-1].add(root2.val)

        dfs(root1, children1)
        dfs(root2, children2)

        return children1 == children2