# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # faster by just dumping the rest of the remaining list
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_head = ListNode()
        node = dummy_head
        node1 = list1
        node2 = list2
    
        while node1 or node2:
            if node1 and node2:
                if node1.val < node2.val:
                    node.next = node1
                    node1 = node1.next
                else:
                    node.next = node2
                    node2 = node2.next
                node = node.next
            elif node1 and not node2:
                while node1:
                    node.next = node1
                    node = node.next
                    node1 = node1.next
            elif not node1 and node2:
                while node2:
                    node.next = node2
                    node = node.next
                    node2 = node2.next
        
        return dummy_head.next

    def mergeTwoLists(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyHead = dummyNode

        while node1 or node2:
            if not node2 or (node1 and node2 and node1.val < node2.val):
                dummyNode.next = node1
                dummyNode = node1
                node1 = node1.next
            elif not node1 or (node1 and node2 and node1.val >= node2.val):
                dummyNode.next = node2
                dummyNode = node2
                node2 = node2.next

        return dummyHead.next
    
    # this is neater
    def mergeTwoLists2(self, node1: Optional[ListNode], node2: Optional[ListNode]) -> Optional[ListNode]:
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

        dummyNode.next = node1 if node1 else node2

        return dummyHead.next