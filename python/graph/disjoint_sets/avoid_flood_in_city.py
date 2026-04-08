# https://leetcode.com/problems/avoid-flood-in-the-city

from typing import List
from sortedcontainers import SortedList

class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        # UnionFind, join used days

        def find(x):
            if x > N:
                return N
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def consume(x):
            # union of x and x + 1
            parent[x] = find(x + 1)

        N = len(rains)
        parent = [i for i in range(N + 1)]
        last_rain_i = {}
        ans = [1] * N

        for i, day in enumerate(rains):
            if day > 0:
                ans[i] = -1
                consume(i)
                if day in last_rain_i:
                    # exactly the property we needed
                    next_dry_day = find(last_rain_i[day] + 1) # this achived earliest possible dry day after the day last_rain_i[day]
                    if next_dry_day > i:
                        return []
                    ans[next_dry_day] = day
                    consume(next_dry_day)
                last_rain_i[day] = i
        
        return ans


    def avoidFlood(self, rains: List[int]) -> List[int]:
        # OrderedList, allows for log n look up of next valid index after another index
        
        N = len(rains)
        last_rain_i = {}
        ans = [-1] * N
        next_dry_day = SortedList()

        for i in range(N):
            if rains[i] == 0:
                next_dry_day.add(i)
                ans[i] = 1 # dry an arbitrary dayfor now, might change later if it turns out we needed to dry a specific day
            else:
                if rains[i] in last_rain_i:
                    to_dry = next_dry_day.bisect_left(last_rain_i[rains[i]]) # next dry day after the last rain time of rains[i]
                    if to_dry == len(next_dry_day): # could not find day to dry
                        return []
                    ans[next_dry_day[to_dry]] = rains[i]
                    next_dry_day.remove(next_dry_day[to_dry])
                last_rain_i[rains[i]] = i

        return ans

s = Solution()
print(s.avoidFlood([1,0,2,0,3,0,2,0,0,0,1,2,3]))
