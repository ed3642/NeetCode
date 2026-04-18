# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # recurse 
        # preorder[0] is always root
        # left of inorder[preorder[0]] is always left tree and inorder[preorder[0] + 1] is right tree
        inorder_index_hm = { num : i for i, num in enumerate(inorder)}
        preorder.reverse()

        # stand and end of inorder list
        def build(start, end):
            if end < start: return None
            root = TreeNode(preorder.pop())
            root_index = inorder_index_hm[root.val]

            root.left = build(start, root_index - 1)
            root.right = build(root_index + 1, end)
            return root
        
        return build(0, len(inorder) - 1)
            
            
