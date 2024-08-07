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
        # store cumulative sum in dict and see how many times this sum has occured so far
        # this is like prefix sum questions but with a binary tree we have to backtrack the prefix sums when processing another branch of the tree

        def dfs(node, total):
            if not node:
                return 0
            
            total += node.val
            
            # path sum starts at the root
            if total == targetSum:
                self.count += 1
            
            # path sum starts somewhere in the middle
            need = total - targetSum # some path in the tree whos sum is targetSum
            if need in prefix_sum:
                self.count += prefix_sum[need]

            prefix_sum[total] += 1
            dfs(node.left, total)
            dfs(node.right, total)
            prefix_sum[total] -= 1

        prefix_sum = defaultdict(int) # <sum, freq>
        prefix_sum[0] = 1 # root node to its self
        self.count = 0
        dfs(root, 0)

        return self.count