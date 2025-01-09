# https://leetcode.com/problems/remove-nth-node-from-end-of-list
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # one pass, O(n) space
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        index_to_node = []

        node = head
        while node:
            index_to_node.append(node)
            node = node.next

        size = len(index_to_node)
        to_remove_i = size - n
        node = index_to_node[to_remove_i]
        if to_remove_i > 0:
            prev = index_to_node[to_remove_i - 1]
            next = node.next
            prev.next = next
        else:
            # remove just the first node
            return head.next

        return head
    
    # 2 passes but O(1) space
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 
        node = head
        for i in range(n):
            node = node.next

        prev = None
        delayed = head
        while node:
            node = node.next
            prev = delayed
            delayed = delayed.next

        if prev:
            prev.next = delayed.next
        else:
            # remove just the first node
            return head.next
        return head