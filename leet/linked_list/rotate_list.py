# https://leetcode.com/problems/rotate-list

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None
        
        size = 0
        node = head
        while node:
            node = node.next
            size += 1

        
        k = k % size
        delayed = head
        node = head
        steps = 0

        while node.next:
            node = node.next
            if steps >= k:
                delayed = delayed.next
            steps += 1
        
        node.next = head
        head = delayed.next
        delayed.next = None

        return head