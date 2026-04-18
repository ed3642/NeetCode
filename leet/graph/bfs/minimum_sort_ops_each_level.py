# https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        # minimum operations to sort arr
        # https://www.geeksforgeeks.org/python-program-for-cycle-sort/
        def cycle_sort(arr):
            # cycle sort is optimal in minimal number of writes to arr
            # an edge is formed when two nodes need to be swapped to be in sorted order
            N = len(arr)
            operations = 0
            sorted_arr = sorted([(num, i) for i, num in enumerate(arr)], key=lambda x: x[0])
            visited = [False] * N

            for i in range(N):
                cycle_edges = 0 # this is actually 1 edge less, but its what we want
                index = i
                while not visited[index] and arr[index] != sorted_arr[index][0]:
                    visited[index] = True
                    cycle_edges += 1
                    # swap the right value into index
                    arr[index], arr[sorted_arr[index][1]] = arr[sorted_arr[index][1]], arr[index]
                    index = sorted_arr[index][1] # where curr elem should be
                operations += cycle_edges
            
            return operations

        q = deque([root])
        total_operations = 0

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            total_operations += cycle_sort(level)

        return total_operations
