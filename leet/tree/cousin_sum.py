# https://leetcode.com/problems/cousins-in-binary-tree-ii/description/
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # i is the pfs_index, prefixsum
        def calc_val(pfs, i):
            if i % 2 == 0:
                left = pfs[i - 2] # skip sibling to left
                right = pfs[-1] - pfs[i]
            else:
                left = pfs[i - 1]
                right = pfs[-1] - pfs[i + 1] # skip sibling to right
            return left + right

        q = deque([root])
        while q:
            level = []
            pfs = [0]
            for _ in range(len(q)):
                node = q.popleft()
                if not node:
                    pfs.append(pfs[-1])
                    level.append(None)
                    continue
                else:
                    pfs.append(pfs[-1] + node.val)
                    level.append(node)
                q.append(node.left)
                q.append(node.right)
            if pfs[-1] == 0: continue
            if len(level) < 3:
                for i, node in enumerate(level):
                    if not node: continue
                    node.val = 0
                continue
            for i, node in enumerate(level):
                if not node: continue
                node.val = calc_val(pfs, i + 1)
        
        return root