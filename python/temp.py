from sortedcontainers import SortedList

class MyCalendarTwo:
    # line sweep events

    def __init__(self):
        self.calendar = SortedList()
        self.events = SortedList()

    def book(self, start: int, end: int) -> bool:
        if self.can_place(start, end):
            self.calendar.add((start, end))
            return True
        return False

    def can_place(self, start, end):
        # line sweep, in this problem, close before opening
        CLOSE = 0
        OPEN = 1
        temp_events = self.events.copy()
        temp_events.add((start, OPEN))
        temp_events.add((end, CLOSE))
        curr_open = 0
        for time, type in temp_events:
            if type == OPEN:
                curr_open += 1
            elif type == CLOSE:
                curr_open -= 1
            if curr_open >= 3:
                return False
        self.events = temp_events
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)