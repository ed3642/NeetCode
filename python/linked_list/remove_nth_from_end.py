# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = head
        node = head
        nodes_list = []
        prev = None
        next = node.next

        while node:
            triplet = tuple([prev, node, next])
            nodes_list.append(triplet)
            prev = node
            node = node.next
            if node:
                next = node.next
        
        prev, node, next = nodes_list[len(nodes_list) - n]
        if not prev and not next and n == 1:
            dummyHead = None
        if prev:
            prev.next = next
        else:
            dummyHead = next

        return dummyHead