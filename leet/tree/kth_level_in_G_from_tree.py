# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree
# Definition for a binary tree node.

from collections import deque
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # makes a tree into a graph just by recording the parent
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # binary tree dfs to mark parent of ancestors
        # -> bfs 3 directions from target

        def dfs(node):
            if node.left:
                parent[node.left] = node
                dfs(node.left)
            if node.right:
                parent[node.right] = node
                dfs(node.right)

        # record parents
        parent = {root: None}
        dfs(root)

        # bfs from target
        level = 0
        q = deque([target])
        visited = set([target.val])
        while q:
            if level == k:
                return [node.val for node in q]
            
            for _ in range(len(q)):
                node = q.popleft()
                if node.left and node.left.val not in visited:
                    visited.add(node.left.val)
                    q.append(node.left)
                if node.right and node.right.val not in visited:
                    visited.add(node.right.val)
                    q.append(node.right)
                if parent[node] and parent[node].val not in visited:
                    visited.add(parent[node].val)
                    q.append(parent[node])
            level += 1
        
        return []