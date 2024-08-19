# https://leetcode.com/problems/ugly-number-ii
import heapq

class Solution:

    # O(n)
    # like merging 3 sorted list
    def nthUglyNumber(self, n: int) -> int:

        uglies = [0] * n
        uglies[0] = 1
        multiplier_pos = {
            2: 0,
            3: 0,
            5: 0,
        }
        next_by_multiplier = {
            2: 2,
            3: 3,
            5: 5,
        }

        for i in range(1, n):
            next_ugly = min(next_by_multiplier.values())
            uglies[i] = next_ugly

            # update the one that made this number
            for key in next_by_multiplier:
                if next_by_multiplier[key] == next_ugly:
                    multiplier_pos[key] += 1
                    next_by_multiplier[key] = uglies[multiplier_pos[key]] * key

        return uglies[n - 1]

    # O(n log n)
    def nthUglyNumber2(self, n: int) -> int:
        
        heap = [1]
        uglies = set([1])
        curr = 1

        for _ in range(n):
            curr = heapq.heappop(heap)

            for mult in [2, 3, 5]:
                cand = curr * mult
                if cand not in uglies:
                    uglies.add(cand)
                    heapq.heappush(heap, cand)
        
        return curr
    
        