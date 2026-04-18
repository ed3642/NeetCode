# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        
        node = head
        if not node or not node.next or not node.next.next:
            return [-1, -1]
        
        earliest_peak_pos = -1
        last_peak_pos = -1
        curr_peak_pos = -1

        res = [float('inf'), -float('inf')]
        last_2 = None
        last = None
        pos = 1
        while node:
            last_2, last, node = last, node, node.next

            if last_2 and last and node:
                if (last_2.val < last.val > node.val) or (last_2.val > last.val < node.val): # is a peak
                    if earliest_peak_pos == -1:
                        earliest_peak_pos = pos
                        last_peak_pos = pos
                    else:
                        curr_peak_pos = pos
                        res[0] = min(curr_peak_pos - last_peak_pos, res[0])
                        last_peak_pos = curr_peak_pos
            pos += 1
        
        res[1] = last_peak_pos - earliest_peak_pos
        if res[0] == float('inf'): # didnt find at least 2 peaks
            return [-1, -1]
        return res
        