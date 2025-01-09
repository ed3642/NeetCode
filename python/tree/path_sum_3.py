from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        # get running sum
        # post order traversal to look for needed children

        def post_order(node, _sum):
            nonlocal count
            if not node:
                return

            need = _sum - targetSum
            count += sum_count[need]

            sum_count[_sum] += 1
            if node.left:
                post_order(node.left, _sum + node.left.val)
            if node.right:
                post_order(node.right, _sum + node.right.val)
            sum_count[_sum] -= 1

        if not root:
            return 0
        # check valid paths
        count = 0
        sum_count = defaultdict(int)
        sum_count[0] = 1
        post_order(root, root.val)
        
        return count
    