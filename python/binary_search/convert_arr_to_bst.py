# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        
        def insert(l, r):
            if l > r:
                return None
            if l == r:
                return TreeNode(nums[l])
            m = (l + r) // 2
            node = TreeNode(nums[m])
            node.left = insert(l, m - 1)
            node.right = insert(m + 1, r)
            return node

        return insert(0, len(nums) - 1)