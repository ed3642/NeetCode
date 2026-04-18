# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# NOTE: there is a pretty involved method: Day-Stout-Warren Algorithm that uses O(1) memory
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            order.append(node.val)
            dfs(node.right)
        
        def build(l, r):
            if l > r:
                return None
            m = (l + r) // 2
            left_tree = build(l, m - 1)
            right_tree = build(m + 1, r)
            new_node = TreeNode(order[m], left=left_tree, right=right_tree)
            return new_node

        order = []
        dfs(root)

        return build(0, len(order) - 1)