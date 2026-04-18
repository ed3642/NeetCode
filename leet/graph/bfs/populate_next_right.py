from collections import deque
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()
                if not node: continue
                if i == level_length - 1:
                    node.next = None
                else:
                    node.next = queue[0]
                queue.append(node.left)
                queue.append(node.right)
        
        return root
    
    def connect2(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(node, next):
            if not node: return

            node.next = next
            dfs(node.left, node.right)
            dfs(node.right, None if not node.next else node.next.left)

        dfs(root, None)
        return root
