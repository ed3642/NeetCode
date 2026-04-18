# Definition for singly-linked list.
from typing import Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummyHead = head
        node = head
        nodes_q = deque()

        while node:
            nodes_q.append(node)
            temp = node.next
            node.next = None
            node = temp

        node = nodes_q.popleft()
        pop_front = False
        while nodes_q:
            if pop_front:
                node.next = nodes_q.popleft()
                node = node.next
                pop_front = False
            else:
                node.next = nodes_q.pop()
                node = node.next
                pop_front = True
