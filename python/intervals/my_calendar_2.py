from sortedcontainers import SortedDict, SortedList

class MyCalendarTwo:
    # line sweep by just keep track of how many things are open at each event
    def __init__(self):
        self.events = SortedDict()

    def book(self, start: int, end: int) -> bool:
        return self.can_place(start, end)

    def can_place(self, start, end):
        # activate this booking by increment the count of OPEN and CLOSE events
        self.events[start] = self.events.get(start, 0) + 1
        self.events[end] = self.events.get(end, 0) - 1

        curr_open = 0
        for time in self.events:
            curr_open += self.events[time]
            if curr_open >= 3:
                # deactive this booking by decrement the count of OPEN and CLOSE events
                self.events[start] -= 1
                self.events[end] += 1
                return False
        return True

class MyCalendarTwo:
    # line sweep events
    def __init__(self):
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        return self.can_place(start, end)

    def can_place(self, start, end):
        # line sweep, in this problem, close before opening
        CLOSE = 0
        OPEN = 1
        self.events.add((start, OPEN))
        self.events.add((end, CLOSE))
        curr_open = 0
        for time, type in self.events:
            if type == OPEN:
                curr_open += 1
            elif type == CLOSE:
                curr_open -= 1
            if curr_open >= 3:
                self.events.remove((start, OPEN))
                self.events.remove((end, CLOSE))
                return False
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)