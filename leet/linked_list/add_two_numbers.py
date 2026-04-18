# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummyhead = ListNode()
        node = dummyhead

        while l1 and l2:
            _sum = l1.val + l2.val + carry
            if _sum > 9:
                carry = 1
                _sum %= 10
            else:
                carry = 0
            l1.val = _sum
            node.next = l1
            node = node.next
            l1 = l1.next
            l2 = l2.next

        # add the rest of the longer list
        while l1:
            _sum = l1.val + carry
            if _sum > 9:
                carry = 1
                _sum %= 10
            else:
                carry = 0
            l1.val = _sum
            node.next = l1
            node = node.next
            l1 = l1.next
        while l2:
            _sum = l2.val + carry
            if _sum > 9:
                carry = 1
                _sum %= 10
            else:
                carry = 0
            l2.val = _sum
            node.next = l2
            node = node.next
            l2 = l2.next
        # add the carry if it exist
        if carry == 1:
            node.next = ListNode(val=carry)
            node = node.next
        
        return dummyhead.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add numbers from l2 to l1 and carry over
        def add_carry_over(node, carry_over, prev):
            while carry_over == 1:
                if not node:
                    node = ListNode()
                    prev.next = node
                total = node.val + carry_over
                carry_over = 0
                if total < 10:
                    node.val = total
                else:
                    carry_over = 1
                    node.val = total - 10
                prev = node
                node = node.next

        node1 = l1
        node2 = l2
        dummyHead1 = l1
        dummyHead2 = l2
        prev1 = l1
        prev2 = l2
        carry_over = 0

        while node1 and node2:
            total = node1.val + node2.val + carry_over
            carry_over = 0
            if total < 10:
                node1.val = total
                node2.val = total
            else:
                carry_over = 1
                node1.val = total - 10
                node2.val = total - 10
            prev1 = node1
            prev2 = node2
            node1 = node1.next
            node2 = node2.next
        
        if not node1:
            add_carry_over(node2, carry_over, prev2)
            return dummyHead2
        elif not node2:
            add_carry_over(node1, carry_over, prev1)
            return dummyHead1
        return dummyHead1


