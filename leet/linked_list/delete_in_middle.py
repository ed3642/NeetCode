# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = head

        if not dummy_head.next:
            return None

        fast = head
        prev_slow = head
        slow = head

        while fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next
            if fast.next: # double jump
                fast = fast.next
        
        prev_slow.next = slow.next # erase slow

        return dummy_head
            