# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # we could improve this by creating a dict of the nodes index in the inorder list
    # and not passing the new subarrays but just the index of the new section
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        
        if len(preorder) == 0:
            return None

        root = preorder[0]
        root_i = inorder.index(root)

        left = self.buildTree(preorder[1:root_i + 1], inorder[:root_i])
        right = self.buildTree(preorder[root_i + 1:], inorder[root_i + 1:])

        return TreeNode(val=root, left=left, right=right)