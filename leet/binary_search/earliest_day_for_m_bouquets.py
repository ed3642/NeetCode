class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:

        def valid_day(day):
            bouquets = 0
            count = 0

            for flower in bloomDay:
                if flower <= day:
                    count += 1
                else:
                    count = 0
                if count == k:
                    bouquets += 1
                    count = 0
            
            return bouquets >= m
        
        # invalid case
        if len(bloomDay) < m * k:
            return -1
        
        days = sorted(set(bloomDay))
        n = len(days)

        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2
            if not valid_day(days[mid]):
                l = mid + 1
            else:
                r = mid
        
        return days[l]
    
s = Solution()
print(s.minDays([7,7,7,7,12,7,7], 2, 3))