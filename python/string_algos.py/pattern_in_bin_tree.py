# https://leetcode.com/problems/linked-list-in-binary-tree
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
    # O(n)
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:

        def dfs(node, to_match):
            if to_match == N:
                return True
            if not node:
                return False
            while to_match > 0 and node.val != pattern[to_match]:
                to_match = lps[to_match - 1]
            if node.val == pattern[to_match]:
                to_match += 1
            return dfs(node.left, to_match) or dfs(node.right, to_match)
        
        pattern = []
        while head:
            pattern.append(head.val)
            head = head.next
        N = len(pattern)
        lps = [0] * N
        to_match = 0
        for end in range(1, N):
            while to_match > 0 and pattern[to_match] != pattern[end]:
                to_match = lps[to_match - 1]
            if pattern[to_match] == pattern[end]:
                to_match += 1
            lps[end] = to_match
        
        return dfs(root, 0)

    # O(n * m)
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def check_path(tree_node, list_node):
            if not list_node:
                return True
            if not tree_node:
                return False
            if tree_node.val == list_node.val:
                return check_path(tree_node.left, list_node.next) or check_path(tree_node.right, list_node.next)
            return False
        
        def dfs(node):
            if not node:
                return False
            if node.val == head.val and check_path(node, head):
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)