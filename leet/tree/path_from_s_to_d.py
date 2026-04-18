# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # post order

        def dfs(node, path, target):
            if not node:
                return False
            
            left = dfs(node.left, path, target)
            right = dfs(node.right, path, target)
            if node.val == target[0]:
                return True
            if left:
                path.append('L')
                return True
            if right:
                path.append('R')
                return True

            return False

        path_to_source = []
        path_to_dest = []
        dfs(root, path_to_source, [startValue])
        dfs(root, path_to_dest, [destValue])
        # remove part of path that is the same from root (prefix), e.g 1 -> source -> dest, we remove the 1
        path_to_source = list(reversed(path_to_source))
        path_to_dest = list(reversed(path_to_dest))
        i = 0
        while i < len(path_to_source) and i < len(path_to_dest) and path_to_source[i] == path_to_dest[i]:
            i += 1
        path_to_source = path_to_source[i:]
        path_to_dest = path_to_dest[i:]
        path_to_source = 'U' * len(path_to_source) # we can only go up from the source
        return path_to_source + ''.join(path_to_dest)
