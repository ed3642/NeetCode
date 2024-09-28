# https://leetcode.com/problems/design-circular-deque/description/
# this kinda misses the point of the problem which was to use a fixed size list and modulos
# but its a nice fixed size queue solution
# NOTE: its better to use a fixed size list for fixed size queues
class Node:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.dummy_center = Node()
        self.dummy_center.prev = self.dummy_center
        self.dummy_center.next = self.dummy_center
        self.count = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        if self.count == 0:
            self.insert_first(new_node)
        else:
            front = self.dummy_center.prev
            front.next = new_node
            new_node.prev = front
            new_node.next = self.dummy_center
            self.dummy_center.prev = new_node
        self.count += 1
        return True   

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        if self.count == 0:
            self.insert_first(new_node)
        else:
            last = self.dummy_center.next
            last.prev = new_node
            new_node.prev = self.dummy_center
            new_node.next = last
            self.dummy_center.next = new_node
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        behind_last = self.dummy_center.prev.prev
        behind_last.next = self.dummy_center
        self.dummy_center.prev = behind_last
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        after_last = self.dummy_center.next.next
        after_last.prev = self.dummy_center
        self.dummy_center.next = after_last
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.dummy_center.prev.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.dummy_center.next.val

    def insert_first(self, first_node):
        first_node.prev = self.dummy_center
        first_node.next = self.dummy_center
        self.dummy_center.prev = first_node
        self.dummy_center.next = first_node
        
    def isEmpty(self) -> bool:
        return self.count == 0
        
    def isFull(self) -> bool:
        return self.count == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()