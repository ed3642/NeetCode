# Definition for a Node.
from collections import deque

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        if not root: return []
        # bfs
        queue = deque([root])
        levels = [[root.val]]

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
                    level.append(child.val)
            if level:
                levels.append(level)

        return levels