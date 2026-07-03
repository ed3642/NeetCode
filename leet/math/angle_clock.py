# https://leetcode.com/problems/angle-between-hands-of-a-clock

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        deg_in_hour = 30
        deg_in_min = 6
        deg_1 = minutes*deg_in_min
        deg_2 = hour*deg_in_hour+((minutes/60)*deg_in_hour)

        res = abs(deg_1-deg_2)
        return res if res <= 180 else 360-res