from sortedcontainers import SortedList

class MyCalendarThree:
    # perfect use of line sweep
    def __init__(self):
        self.events = SortedList()

    def book(self, startTime: int, endTime: int) -> int:
        # line sweep, in this problem, close before opening
        CLOSE = 0
        OPEN = 1
        self.events.add((startTime, OPEN))
        self.events.add((endTime, CLOSE))
        curr_open = 0
        max_open = 0
        for time, type in self.events:
            if type == OPEN:
                curr_open += 1
            elif type == CLOSE:
                curr_open -= 1
            max_open = max(curr_open, max_open)
        return max_open

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)