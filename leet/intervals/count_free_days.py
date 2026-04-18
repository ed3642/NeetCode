# https://leetcode.com/problems/count-days-without-meetings

from typing import List

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        count = 0
        meetings.sort(key=lambda x: x[0])
        prev_end = 0

        for start, end in meetings:
            space = start - prev_end - 1
            count += space if space > 0 else 0
            prev_end = max(end, prev_end)
        # last space of days
        space = days - prev_end
        count += space if space > 0 else 0

        return count