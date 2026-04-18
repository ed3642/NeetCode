from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # there is an O(1) space solution but this is good
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        seen = set()
        node1 = headA
        node2 = headB

        while node1 or node2:
            if node1 and node2:
                if node1 == node2: # perfect intersect
                    return node1
                if node1 in seen:
                    return node1
                elif node2 in seen:
                    return node2
                seen.add(node1)
                seen.add(node2)
                node1 = node1.next
                node2 = node2.next
            elif node1 and not node2:
                if node1 in seen:
                    return node1
                seen.add(node1)
                node1 = node1.next
            elif not node1 and node2:
                if node2 in seen:
                    return node2
                seen.add(node2)
                node2= node2.next
        
        return None