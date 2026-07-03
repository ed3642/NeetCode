# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        node = head
        list = []
        max_sum = -float('inf')

        while node:
            list.append(node.val)
            node = node.next
        
        n = len(list)
        for i in range(n):
            max_sum = max(list[i]+list[n-1-i], max_sum)
        
        return max_sum

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # reverse second half
        # go over pairs with the other half reversed

        def reverse(head):
            if not head:
                return None
            
            prev = None

            while head:
                temp = head.next
                head.next = prev
                prev = head
                head = temp
            
            return prev

        slow = head
        fast = head
        head1 = head

        while fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow.next is the first node of the second half
        head2 = reverse(slow.next)

        # check the pairs easily now
        _max = -float('inf')
        while head2:
            total = head1.val + head2.val
            _max = max(_max, total)
            head1 = head1.next
            head2 = head2.next
        
        return _max