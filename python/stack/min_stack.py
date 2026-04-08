# https://leetcode.com/problems/min-stack
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val_i = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_val_i or val < self.stack[self.min_val_i[-1]]:
            self.min_val_i.append(len(self.stack) - 1)

    def pop(self) -> None:
        self.stack.pop()
        if self.min_val_i and self.min_val_i[-1] == len(self.stack):
            self.min_val_i.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_val_i[-1]]

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_mono_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_mono_stack or val <= self.min_mono_stack[-1]:
            self.min_mono_stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if self.min_mono_stack and popped == self.min_mono_stack[-1]:
            self.min_mono_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_mono_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# param_4 = obj.getMin()
# obj.pop()
# param_3 = obj.top()