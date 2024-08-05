
# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 2 passes
        # store nodes in first pass in hm
        # connect new nodes in second pass
        if not head: return None

        hm = dict()
        dummyHead = Node(0)
        dummyHead.next = head
        hm[head] = dummyHead
        node = head

        # record nodes
        while node:
            new_node = Node(node.val)
            hm[node] = new_node
            node = node.next

        # connect nodes
        node = head
        dummyHead.next = hm.get(head)
        while node:
            new_node = hm.get(node)
            if not new_node:
                node = node.next
                continue
            if node.next:
                new_node.next = hm.get(node.next)
            if node.random:
                new_node.random = hm.get(node.random)
            node = node.next
        
        return dummyHead.next