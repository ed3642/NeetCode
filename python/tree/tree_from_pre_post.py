# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        # 2,5
        # 5,2
        if not preorder:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        post_left_root_i = postorder.index(preorder[1])
        left = self.constructFromPrePost(
            preorder[1:post_left_root_i + 2],
            postorder[:post_left_root_i + 1])
        
        right = self.constructFromPrePost(
            preorder[post_left_root_i + 2:], 
            postorder[post_left_root_i + 1:len(postorder) - 1])
        
        return TreeNode(preorder[0], left, right)


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)