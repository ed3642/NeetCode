# https://leetcode.com/problems/merge-k-sorted-lists
import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class HeapItem:
    # need this since we cant compare ListNodes, we are not allowed to change the ListNode definition
    def __init__(self, node=None):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None

        dummy_head = ListNode()
        heap = []

        # add the heads to the heap
        for node in lists:
            if not node:
                continue
            heapq.heappush(heap, HeapItem(node))

        # add each min node and replace it with the next in its list
        node = dummy_head
        while heap:
            heap_item = heapq.heappop(heap)
            min_node = heap_item.node
            next_list_node = min_node.next
            if next_list_node:
                heapq.heappush(heap, HeapItem(next_list_node))
            node.next = min_node
            node = node.next
        
        return dummy_head.next

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