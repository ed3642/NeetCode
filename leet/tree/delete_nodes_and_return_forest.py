# https://leetcode.com/problems/delete-nodes-and-return-forest/
from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        
        # puts node in a list to be deleted once we are at that node
        def lazy_check_children(parent):
            if parent.left and parent.left.val in to_delete:
                to_delete_parents[parent.left] = parent
            if parent.right and parent.right.val in to_delete:
                to_delete_parents[parent.right] = parent

        def delete_child(child):
            parent = to_delete_parents[child]
            if parent.left == child:
                parent.left = None
            elif parent.right == child:
                parent.right = None
            if child.left:
                roots.append(child.left)
            if child.right:
                roots.append(child.right)

        def dfs(node):
            if not node:
                return None
            
            lazy_check_children(node)

            dfs(node.left)
            dfs(node.right)

            if node.val in to_delete:
                delete_child(node)

        dummy_root = TreeNode(val=0, left=root) # we might have to delete the original root
        roots = [root] if root.val not in to_delete else []
        to_delete = set(to_delete)
        to_delete_parents = defaultdict(TreeNode)
        dfs(dummy_root)
        return roots