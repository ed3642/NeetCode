# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.i = 0
        self.order = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.order.append(node.val)
            dfs(node.right)
        
        dfs(root)
            

    def next(self) -> int:
        if self.i < len(self.order):
            val = self.order[self.i]
            self.i += 1
            return val

    def hasNext(self) -> bool:
        if self.i < len(self.order):
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()