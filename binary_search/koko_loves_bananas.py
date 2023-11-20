import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def eatingTime(rate) -> int:
            total = 0
            for pile in piles:
                if total > h: # wont have enough time
                    return float('inf')
                total += math.ceil(pile / rate)
            return total if total <= h else float('inf')

        piles.sort()
        biggest = piles[-1]
        smallest = math.ceil(biggest / h)
        smallest_rate = float('inf')

        while smallest < biggest:
            rate = (smallest + biggest) // 2
            time = eatingTime(rate)
            if h < time:
                smallest = rate - 1
            elif h > time:
                biggest = rate
            else:
                smallest_rate = min(rate, smallest_rate)
                biggest = smallest_rate
        
        return smallest_rate if smallest_rate != float('inf') else smallest
    
    def minEatingSpeed2(self, piles: list[int], h: int) -> int:
        def eatingTime(rate) -> int:
            total = 0
            for pile in piles:
                if total > h: # wont have enough time
                    return float('inf')
                total += math.ceil(pile / rate)
            return total if total <= h else float('inf')
        
        total_bananas = sum(piles)
        slowest_rate = math.ceil(total_bananas / h) # evenly distributed, slowest rate but might not finish in time
        fastest_rate = math.ceil(total_bananas / (h - len(piles) + 1)) # all one pile, eat as slow as possible
        abs_slowest_rate = float('inf')

        while slowest_rate < fastest_rate:
            mid = (slowest_rate + fastest_rate) // 2
            time = eatingTime(mid)

            if time < h:
                fastest_rate = mid
            elif time > h:
                slowest_rate = mid + 1
            else:
                abs_slowest_rate = min(mid, abs_slowest_rate)
                fastest_rate = abs_slowest_rate

        return abs_slowest_rate if abs_slowest_rate != float('inf') else slowest_rate



s = Solution()

piles = [1,11,13,8]
print(s.minEatingSpeed2(piles, 8))