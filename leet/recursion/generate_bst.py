# https://leetcode.com/problems/unique-binary-search-trees-ii

# Definition for a binary tree node.
from functools import cache
from typing import List, Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
    
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def build(l, r):
            if l > r:
                return (None,)
            
            res = []
            for num in range(l, r+1):
                left = build(l, num-1)
                right = build(num+1, r)

                for lnode in left:
                    for rnode in right:
                        node = TreeNode(num)
                        node.left = lnode
                        node.right = rnode
                        res.append(node)
            return tuple(res)

        return build(1, n)