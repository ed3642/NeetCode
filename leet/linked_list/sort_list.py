# https://leetcode.com/problems/sort-list
import heapq
import random
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class ComparableNode:
    def __init__(self, node=None):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    # O(n log n)
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        heap = []

        node = head
        while node:
            heapq.heappush(heap, ComparableNode(node))
            node = node.next
        
        dummy_head = ListNode()
        node = dummy_head
        while heap:
            heap_item = heapq.heappop(heap)
            popped_node = heap_item.node
            popped_node.next = None # break the old links
            node.next = popped_node
            node = node.next
        
        return dummy_head.next

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # transform into arr and quicksort
        # this logic works but TLE

        def quicksort(l, r):
            if l >= r:
                return 
            
            pivot_i = partition(l, r)

            quicksort(l, pivot_i - 1)
            quicksort(pivot_i + 1, r)

        def partition(l, r):
            rand_i = random.randint(l, r)
            arr[r], arr[rand_i] = arr[rand_i], arr[r] # put pivot at r
            pivot = arr[r]
            placer_i = l
            for i in range(l, r):
                if arr[i] < pivot:
                    arr[placer_i], arr[i] = arr[i], arr[placer_i] 
                    placer_i += 1
            arr[placer_i], arr[r] = arr[r], arr[placer_i] # final swap
            return placer_i # final index of pivot
            
        if not head:
            return None 
        
        node = head
        arr = []
        while node:
            arr.append(ComparableNode(node))
            node = node.next
        
        quicksort(0, len(arr) - 1)

        for i in range(1, len(arr)):
            arr[i].node.next = None # break old links
            arr[i - 1].node.next = arr[i].node

        return arr[0].node

