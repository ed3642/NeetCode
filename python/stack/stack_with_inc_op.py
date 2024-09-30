# https://leetcode.com/problems/design-a-stack-with-increment-operation/
class CustomStack:
    # O(1) all operations
    # lazy propagation of increments
    def __init__(self, maxSize: int):
        self.stack = []
        self.increments = []
        self.max_size = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.max_size:
            self.stack.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        inc = self.increments.pop()
        total = self.stack.pop() + inc
        # lazy inc propagation
        if len(self.increments) > 0:
            self.increments[-1] += inc
        return total

    def increment(self, k: int, val: int) -> None:
        i = min(k, len(self.stack)) - 1
        if i >= 0:
            self.increments[i] += val