from collections import defaultdict


class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: list[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: list[int]) -> int:
        # if there is a valid square, mult each of the counts of the 3 other points that make the square, this calculates the number of ways to complete this square.
        if len(self.points) < 3:
            return 0
        
        count = 0
        x = point[0]
        y = point[1]
        possible_points = list(self.points.keys()) # do this since the dict size might change when checking values that dont exist
        for xi1, yi1 in possible_points:
            if x == xi1 and y != yi1: # vert match. 1st point
                # from here we can calculate where the other points should be
                side_len = abs(y - yi1)
                yi2 = y
                # 2nd point, can be to the left or right
                for mult in range(-1, 2, 2): # checks -1, and 1
                    xi2 = x + (side_len * mult)
                    
                    if (xi2, yi1) in self.points: # 3rd point
                        count += self.points[(xi1, yi1)] * self.points[(xi2, yi2)] * self.points[(xi2, yi1)]
        return count

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)