# https://leetcode.com/problems/swap-nodes-in-pairs
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy_head = ListNode(next=head)

        node = head
        prev = dummy_head

        while node and node.next:
            a = node
            b = node.next
            next = b.next

            prev.next = b
            b.next = a
            a.next = next

            prev = a
            node = next

        return dummy_head.next