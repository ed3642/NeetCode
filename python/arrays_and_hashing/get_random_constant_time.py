# https://leetcode.com/problems/insert-delete-getrandom-o1
from collections import defaultdict
import random

class RandomizedSet:

    def __init__(self):
        self.values = [] # val at each index
        self.val_index = defaultdict(int) # index of each val

    def insert(self, val: int) -> bool:
        if val not in self.val_index:
            self.val_index[val] = len(self.values)
            self.values.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.val_index:
            n = len(self.values)
            index = self.val_index[val]
            if index != n - 1:
                # put the value we want to delete at the end
                last_val = self.values[n - 1]
                self.values[index] = last_val
                self.val_index[last_val] = index
            # delete the last value
            self.values.pop()
            del self.val_index[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.values)

# Your RandomizedSet object will be instantiated and called as such:
