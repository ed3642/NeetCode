from collections import deque

class StockSpanner:
    # mono dec stack in order of input
    def __init__(self):
        self.stack = deque([(float('inf'), -1)]) # act as a cap for day -1
        self.current_day = 0

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        
        span = self.current_day - self.stack[-1][1] # last day bigger than today
        self.stack.append((price, self.current_day))

        self.current_day += 1
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)