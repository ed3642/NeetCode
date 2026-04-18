# https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
from collections import defaultdict
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        
        def dfs(node, level):
            left = 0
            right = 0
            if node.left:
                left = dfs(node.left, level + 1)
            if node.right:
                right = dfs(node.right, level + 1)
            best_reach = max(left, right, level)
            node_level[node.val] = level
            node_reach[node.val] = best_reach
            level_reach_count[level][best_reach] += 1
            # keep track of the best 2
            if len(best_level_reach[level]) == 0:
                best_level_reach[level].append(best_reach)
            elif len(best_level_reach[level]) == 1:
                if best_level_reach[level][0] < best_reach:
                    best_level_reach[level].append(best_level_reach[level][0])
                    best_level_reach[level][0] = best_reach
                else:
                    best_level_reach[level].append(best_reach)
            elif best_reach > best_level_reach[level][0]:
                best_level_reach[level][1] = best_level_reach[level][0]
                best_level_reach[level][0] = best_reach
            elif best_reach > best_level_reach[level][1]:
                best_level_reach[level][1] = best_reach
            return best_reach

        # get node reach
        node_level = {}
        node_reach = {}
        level_reach_count = defaultdict(lambda: defaultdict(int))
        best_level_reach = defaultdict(list)
        dfs(root, 0)

        res = []
        for q in queries:
            level = node_level[q]
            blr = best_level_reach[level][0]
            reach = node_reach[q]
            if blr > reach:
                res.append(blr)
            elif blr == reach:
                if level_reach_count[level][reach] - 1 == 0:
                    if len(level_reach_count[level]) > 1:
                        res.append(best_level_reach[level][1]) # next best on this level
                    else:
                        res.append(level - 1)
                else:
                    res.append(reach)

        return res