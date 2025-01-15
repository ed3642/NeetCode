# https://leetcode.com/problems/linked-list-cycle-ii
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                if slow == fast:
                    return slow
                while True:
                    slow = slow.next
                    fast = fast.next
                    if slow == fast:
                        return slow

        return None