# https://leetcode.com/problems/my-calendar-i/
import bisect 
from sortedcontainers import SortedList

class MyCalendar:
    # in this problem just using a normal list and inserting in O(n) is better than the sorted list O(logn) insert due to the overhead
    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_left(self.calendar, start, key=lambda x: x[0]) # insert based on start
        if index >= 1 and self.calendar[index - 1][1] > start: # starts before prev ends
            return False
        if index < len(self.calendar) and end > self.calendar[index][0]: # ends after next one starts
            return False
        # good to insert
        self.calendar.insert(index, (start, end))
        return True

class MyCalendar:

    def __init__(self):
        self.calendar = SortedList()

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect_left(self.calendar, start, key=lambda x: x[0]) # insert based on start
        if index >= 1 and self.calendar[index - 1][1] > start: # starts before prev ends
            return False
        if index < len(self.calendar) and end > self.calendar[index][0]: # ends after next one starts
            return False
        # good to insert
        self.calendar.add((start, end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)