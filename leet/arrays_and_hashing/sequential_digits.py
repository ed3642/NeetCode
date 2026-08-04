# https://leetcode.com/problems/sequential-digits

from typing import List

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        res = []
        max_root = 10-len(str(low))
        size_buckets = [[] for _ in range(11)] # buckets by digits in num
        
        for x in range(1, max_root+1):
            y = x
            while y <= high:
                next_digit = (y%10)+1
                if next_digit == 10:
                    break
                y = y*10+next_digit
                if low <= y and y <= high:
                    if y > 1000000000:
                        size_buckets[10].append(y)
                    elif y > 100000000:
                        size_buckets[9].append(y)
                    elif y > 10000000:
                        size_buckets[8].append(y)
                    elif y > 1000000:
                        size_buckets[7].append(y)
                    elif y > 100000:
                        size_buckets[6].append(y)
                    elif y > 10000:
                        size_buckets[5].append(y)
                    elif y > 1000:
                        size_buckets[4].append(y)
                    elif y > 100:
                        size_buckets[3].append(y)
                    else: # problem makes all nums be in [10, 10^9]
                        size_buckets[2].append(y)

        for size in range(2, 11):
            res.extend(size_buckets[size])

        return res