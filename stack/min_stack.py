class MinStack:
    # normal stack but it keeps track of the minimum value to return in O(1)

    def __init__(self):
        self.values = []
        self.min_vals = []

    def push(self, val: int) -> None:
        if self.min_vals:
            self.min_vals.append(min(val, self.getMin()))
        else:
            self.min_vals.append(val)
        self.values.append(val)

    def pop(self) -> None:
        self.min_vals.pop()
        self.values.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_vals[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-10)
obj.push(14)
obj.push(-20)
print(obj.top())
obj.pop()
print(obj.getMin())
