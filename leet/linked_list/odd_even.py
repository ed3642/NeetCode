# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        odd = head
        even = head.next
        prev_odd = odd
        prev_even = even
        head_even = even

        while even and odd:
            # move them up by 2, unless they point to null
            even = even.next
            if even:
                even = even.next
            odd = odd.next
            if odd:
                odd = odd.next
            # attach prev to current
            prev_even.next = even
            prev_odd.next = odd
            prev_even = even
            if odd: # make sure this doesnt point to null for the last part
                prev_odd = odd
        
        # put evens at the front
        prev_odd.next = head_even

        return head