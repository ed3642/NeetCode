# Definition for singly-linked list.
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        length = 0
        node = head
        while head:
            length += 1
            head = head.next
        
        res = [None] * k
        block_size = length // k
        to_distribute = length % k

        i = 0
        next_node = node
        while next_node:
            node = next_node
            res[i] = node
            if block_size > 0:
                for _ in range(block_size - 1):
                    node = node.next
                if to_distribute > 0:
                    node = node.next
                    to_distribute -= 1
            # detach tail of this block
            if node:
                next_node = node.next
                node.next = None
            i += 1
        
        return res