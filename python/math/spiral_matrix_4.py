# https://leetcode.com/problems/spiral-matrix-iv/
# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        
        def is_valid(i, j):
            return (i >= min_i and i < max_i and
                    j >= min_j and j < max_j)

        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curr_dir = 0
        i = 0
        j = 0
        min_i = 0
        min_j = 0
        max_i = m
        max_j = n

        while head:
            matrix[i][j] = head.val
            head = head.next
            n_i = i + directions[curr_dir][0]
            n_j = j + directions[curr_dir][1]

            if is_valid(n_i, n_j):
                i = n_i
                j = n_j
            else: # next dir
                # update bounds
                if curr_dir == 0:
                    min_i += 1
                elif curr_dir == 1:
                    max_j -= 1
                elif curr_dir == 2:
                    max_i -= 1
                else:
                    min_j += 1
                # change dir
                curr_dir = (curr_dir + 1) % 4
                i += directions[curr_dir][0]
                j += directions[curr_dir][1]
        
        return matrix