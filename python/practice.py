# https://leetcode.com/problems/linked-list-in-binary-tree
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string string matching prerequisite
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # TODO: solve with kmp string matching
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def check_path(tree_node, list_node):
            if not list_node:
                return True
            if not tree_node:
                return False
            
            if tree_node.val == list_node.val:
                if check_path(tree_node.left, list_node.next) or check_path(tree_node.right, list_node.next):
                    return True
            
            return False

        def dfs(node):
            if not node:
                return False
            if check_path(node, head):
                return True
            
            return dfs(node.left) or dfs(node.right)

        return dfs(root)