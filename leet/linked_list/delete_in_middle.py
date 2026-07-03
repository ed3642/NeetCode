# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return None

        slow = head 
        prev_slow = None
        fast = head.next

        while fast:
            prev_slow = slow
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next

        # delete node and stitch the list
        prev_slow.next = slow.next if slow else None

        return head

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = head

        if not dummy_head.next:
            return None

        fast = head
        prev_slow = head
        slow = head

        while fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next
            if fast.next: # double jump
                fast = fast.next
        
        prev_slow.next = slow.next # erase slow

        return dummy_head
            