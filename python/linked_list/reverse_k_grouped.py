# https://leetcode.com/problems/reverse-nodes-in-k-group

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse_group(left_anchor, curr):
            
            processed = 0
            first = curr
            prev = None
            next = None

            while curr and processed < k:
                next = curr.next
                curr.next = prev 
                prev = curr
                curr = next
                processed += 1
            
            left_anchor.next = prev
            first.next = curr

            return first, curr
        
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1
        
        left_anchor = ListNode()
        first_group_head = left_anchor
        curr = head
        can_fit = size // k
        for _ in range(can_fit):
            last, right_anchor = reverse_group(left_anchor, curr)
            curr = right_anchor
            left_anchor = last
        
        return first_group_head.next
    