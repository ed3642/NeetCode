# Definition for singly-linked list.
from typing import Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummyHead = ListNode()
        head = dummyHead

        # make heap
        index = 0 # to avoid list comparisons in heap
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, index, node))
                index += 1
        
        # LL from heap
        while heap:
            _, index, node = heapq.heappop(heap)
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
            head.next = node
            head = head.next
        
        return dummyHead.next