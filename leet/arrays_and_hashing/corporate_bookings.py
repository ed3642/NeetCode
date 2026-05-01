# https://leetcode.com/problems/corporate-flight-bookings

from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        diff = [0] * (n + 2)

        for i in range(len(bookings)):
            l, r, val = bookings[i]
            # this is the key idea behind diff array to apply a val on [l, r]
            diff[l] += val # turn on the difference at index l
            diff[r + 1] -= val # turn off the difference at index r + 1
        
        for i in range(1, n + 1):
            diff[i] += diff[i - 1]
        
        return diff[1:n + 1]
    

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # classic diff array
        diff_arr = [0] * (n + 2)
        res = [0] * n

        for l, r, delta in bookings:
            diff_arr[l] += delta
            diff_arr[r + 1] -= delta

        _sum = 0
        for i in range(1, n + 1):
            _sum += diff_arr[i]
            res[i - 1] = _sum

        return res