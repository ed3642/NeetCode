# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        
        # post order
        # check dist of all children from left and right

        def dfs(node):
            nonlocal num_pairs
            if not node:
                return [] # no pairs
            
            if node.left == None and node.right == None:
                return [1] # a leaf node, 1 away from its parent
            
            left = dfs(node.left)
            right = dfs(node.right)
            for i in range(len(left)):
                for j in range(len(right)):
                    if left[i] + right[j] <= distance:
                        num_pairs += 1
                    else: # if the sum is too big, and the lists are sorted, we can never get a smaller sum,
                        # so early break
                        break

            # update distances
            # optimization: sorting makes it so we can early break in the pair matching
            return sorted(map(lambda x: x + 1, left + right)) # add 1 to all of them and sort

        num_pairs = 0
        dfs(root)
        return num_pairs