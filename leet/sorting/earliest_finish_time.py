# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i

from typing import List

class Solution:

    # O(n)
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        n = len(landStartTime)
        m =  len(waterStartTime)

        min_time = float('inf')
        land_finish = float('inf')
        for i in range(n):
            land_finish = min(landStartTime[i]+landDuration[i], land_finish)
        for i in range(m):
            if waterStartTime[i] < land_finish:
                min_time = min(land_finish+waterDuration[i], min_time)
            else:
                wait_time = waterStartTime[i]-land_finish
                min_time = min(land_finish+waterDuration[i]+wait_time, min_time)

        water_finish = float('inf')
        for i in range(m):
            water_finish = min(waterStartTime[i]+waterDuration[i], water_finish)
        for i in range(n):
            if landStartTime[i] < water_finish:
                min_time = min(water_finish+landDuration[i], min_time)
            else:
                wait_time = landStartTime[i]-water_finish
                min_time = min(water_finish+landDuration[i]+wait_time, min_time)
        
        return min_time
