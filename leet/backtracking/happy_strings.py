# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n
from collections import defaultdict

class Solution:
    def __init__(self):
        self.happy_strings = []
        self.bt([])
        self.by_lengths = defaultdict(list)
        for string in self.happy_strings:
            self.by_lengths[len(string)].append(string)

    def getHappyString(self, n: int, k: int) -> str:

        happy_strings = self.by_lengths[n]
        if len(happy_strings) < k:
            return ''
        arr = happy_strings[k - 1]

        return ''.join(arr)

    # gen all happy strings size 1 to 10
    def bt(self, builder):
        if len(builder) > 0:
            self.happy_strings.append(builder.copy())
        if len(builder) >= 10:
            return

        for c in 'abc':
            if builder and c == builder[-1]:
                continue
            builder.append(c)
            self.bt(builder)
            builder.pop()
