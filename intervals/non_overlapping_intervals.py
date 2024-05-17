class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # greedy
        # sort by the end time
        # keep the smallest end times first
        # intuition is that the earlier it ends the less events that will overlap it

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        last_end = intervals[0][1]
        removing = 0

        # skip the first interval since its our starting case
        for start, end in intervals[1:]:
            if start < last_end:
                removing += 1
            else:
                last_end = end

        return removing