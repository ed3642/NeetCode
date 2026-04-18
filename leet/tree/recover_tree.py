# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        
        def dfs(node, depth):
            if not order:
                return

            if order[-1][0] == depth:
                new_node_val = order[-1][1]
                order.pop()
                node.left = TreeNode(int(new_node_val))
                dfs(node.left, depth + 1)
            if order and order[-1][0] == depth:
                new_node_val = order[-1][1]
                order.pop()
                node.right = TreeNode(int(new_node_val))
                dfs(node.right, depth + 1)

        def parse_num(i):
            start = i
            while i < N and traversal[i].isdigit():
                i += 1
            return i, traversal[start:i]

        def parse_depth(i):
            start = i
            while i < N and traversal[i] == '-':
                i += 1
            return i, i - start
        
        N = len(traversal)
        order = [0] # depth of the root
        i = 0
        while i < N:
            if traversal[i] == '-':
                i, depth = parse_depth(i)
                order.append(depth)
            else:
                i, num = parse_num(i)
                order[-1] = (order[-1], num)

        order.reverse() # now has (depth, node)
        root = TreeNode(int(order[-1][1]))
        order.pop() # pop the root node

        dfs(root, 1)

        return root

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)