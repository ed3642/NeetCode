# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyHead = dummyNode

        while node1 and node2:
            if node1.val < node2.val:
                dummyNode.next = node1
                dummyNode = node1
                node1 = node1.next
            else:
                dummyNode.next = node2
                dummyNode = node2
                node2 = node2.next
        
        dummyNode.next = node1 if not node2 else node2

        return dummyHead.next