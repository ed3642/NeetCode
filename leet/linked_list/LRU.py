# https://leetcode.com/problems/lru-cache

from collections import defaultdict

# 2026
class Node:
    def __init__(self, key, val=''):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.dummy_start = Node(-1)
        self.dummy_end = Node(-2)
        self.dummy_start.next = self.dummy_end
        self.dummy_end.prev = self.dummy_start
        self.nodes = {} # key -> node
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self.refresh_node(self.nodes[key])
        return self.nodes[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.refresh_node(self.nodes[key])
            self.nodes[key].val = value
            return

        new_node = Node(key, value)
        self.nodes[key] = new_node
        if len(self.nodes) <= self.cap:
            self.put_node(new_node)
        else:
            to_delete = self.dummy_end.prev
            self.delete_node(to_delete)
            self.put_node(new_node)
            del self.nodes[to_delete.key]

    def delete_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def put_node(self, node):
        next = self.dummy_start.next
        self.dummy_start.next = node
        node.prev = self.dummy_start
        next.prev = node
        node.next = next
    
    def refresh_node(self, node):
        self.delete_node(node)
        self.put_node(node)

# 2024
class Node:
    def __init__(self, key=-1, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.elems = defaultdict(int)
        self.left_bound = Node()
        self.right_bound = Node()
        self.capacity = capacity

        self.left_bound.next = self.right_bound
        self.right_bound.prev = self.left_bound

    def get(self, key: int) -> int:
        if key not in self.elems:
            return -1
        
        self.move_node_to_end(self.elems[key])

        return self.elems[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.elems:
            node = self.elems[key]
            node.val = value
            self.move_node_to_end(self.elems[key])
        else:
            new_node = Node(key=key, val=value)
            self.elems[key] = new_node
            if len(self.elems) > self.capacity:
                lru_node = self.left_bound.next
                next = lru_node.next
                del self.elems[lru_node.key]
                self.left_bound.next = next
                next.prev = self.left_bound
            # put new node at end of LL
            self.put_node_at_end(new_node)

    def move_node_to_end(self, node):
        # stitch prev neighbors together
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        # put node at the end of LL
        self.put_node_at_end(node)
    
    def put_node_at_end(self, node):
        last = self.right_bound.prev
        last.next = node
        node.prev = last
        node.next = self.right_bound
        self.right_bound.prev = node

# 2023
class Node:
    def __init__(self, prev=None, next=None, key=0, val=0):
        self.prev = prev
        self.next = next
        self.key = key
        self.val = val

class LRUCache:
    # double LL to keep track of LRU
    # HM to get and set values
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = dict() # <int_key, node>
        self.dummy_head = Node()
        self.dummy_tail = Node()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key in self.hm:
            self.updateNode(key)
            return self.hm[key].val
        return -1
    
    def updateNode(self, key, val=None):
        node = self.hm[key]
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        if val:
            node.val = val
        self.insertNodeAtHead(node)
    
    def insertNodeAtHead(self, node):
        next = self.dummy_head.next
        self.dummy_head.next = node
        next.prev = node
        node.next = next
        node.prev = self.dummy_head

    def deleteNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.hm.pop(node.key)

    def put(self, key: int, value: int) -> None:
        if key in self.hm: # update node
            # update usage, bring to head of LL
            self.updateNode(key, value)
            return

        new_node = Node(key=key, val=value)
        if len(self.hm) < self.cap: # brand new node
            self.insertNodeAtHead(new_node)
        else: # make space for new node
            lru = self.dummy_tail.prev
            self.deleteNode(lru)
            self.insertNodeAtHead(new_node)
        self.hm[key] = new_node