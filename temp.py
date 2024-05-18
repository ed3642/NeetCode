# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        def dfs(node, total):
            if not node:
                return 0
            
            total += node.val
            
            need = total - targetSum
            if need in prefix_sum:
                self.count += prefix_sum[need]

            prefix_sum[total] += 1
            dfs(node.left, total)
            dfs(node.right, total)
            prefix_sum[total] -= 1

        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        self.count = 0
        dfs(root, 0)

        return self.count