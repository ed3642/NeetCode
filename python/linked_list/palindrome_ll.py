from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # we can do it in O(1) space by using fast and slow to find the middle of the list
    # then reversing the first half and comparing the reversed with the rest of the list
    # that the slow ptr didnt get to
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        def reverse_list(head):
            prev = None
            node = head

            while node:
                original_order.append(node)
                temp = node.next
                node.next = prev
                prev = node
                node = temp

            return prev

        original_order = []
        reversed_list = reverse_list(head)

        for i in range(len(original_order) // 2):
            if original_order[i].val != reversed_list.val:
                return False
            reversed_list = reversed_list.next
        
        return True