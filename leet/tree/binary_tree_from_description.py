# https://leetcode.com/problems/create-binary-tree-from-descriptions/
# Definition for a binary tree node.
from typing import Optional
from collections import defaultdict
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        nodes = defaultdict(TreeNode)
        cand_root = set() # only one node should not be a child of anyone, that is the root
        not_root = set()

        for parent, child, isleft in descriptions:
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if child not in nodes:
                nodes[child] = TreeNode(child)
            cand_root.add(parent)
            not_root.add(child)

            if isleft:
                nodes[parent].left = nodes[child]
            else:
                nodes[parent].right = nodes[child]
        
        root = (cand_root-not_root).pop()
        return nodes[root]

    def createBinaryTree(self, descriptions: list[list[int]]) -> Optional[TreeNode]:
        
        nodes = {}
        root_candidates = set()
        for parent, child, is_left in descriptions:
            parent_node = None
            if parent in nodes:
                parent_node = nodes[parent]
            else:
                parent_node = TreeNode(parent)
                root_candidates.add(parent)

            if child in nodes:
                if is_left:
                    parent_node.left = nodes[child]
                else:
                    parent_node.right = nodes[child]
            else:
                child_node = TreeNode(child)
                nodes[child] = child_node
                if is_left:
                    parent_node.left = child_node
                else:
                    parent_node.right = child_node

            if child in root_candidates:
                root_candidates.remove(child)
            if parent not in nodes:
                nodes[parent] = parent_node
        
        root = root_candidates.pop() # should only be one left
        return nodes[root]
            