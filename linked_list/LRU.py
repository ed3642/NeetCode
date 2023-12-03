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