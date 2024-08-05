class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        
        if len(points) == 1:
            return 1

        intervals = sorted(points, key=lambda x: x[1])
        last_end = intervals[0][1]
        need = 1

        for start, end in intervals[1:]:
            if start > last_end:
                need += 1
                last_end = end

        return need