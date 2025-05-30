# https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time

import heapq
from typing import List

class Solution:
    # best
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        
        N = len(passingFees)
        adj_list = [[] for _ in range(N)]
        fees = [float('inf')] * N # fees[node]
        times = [float('inf')] * N # times[node]
        fees[0] = passingFees[0]
        times[0] = 0
        heap = [(passingFees[0], 0, 0)] # cost, time, node

        for _from, _to, time in edges:
            adj_list[_from].append((_to, time))
            adj_list[_to].append((_from, time))

        while heap:
            fee, t, node = heapq.heappop(heap)

            if node == N - 1:
                return fee

            for nei, nei_t in adj_list[node]:
                cand_t = t + nei_t
                if cand_t <= maxTime and cand_t < times[nei]:
                    cand_fee = fee + passingFees[nei]
                    times[nei] = cand_t
                    fees[nei] = cand_fee
                    heapq.heappush(heap, (cand_fee, cand_t, nei))

        return -1

    # slow
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:
        
        N = len(passingFees)
        adj_list = [[] for _ in range(N)]
        fees = [[float('inf') for _ in range(maxTime + 1)] for _ in range(N)] # fees[node][time]
        fees[0][0] = passingFees[0]
        heap = [(passingFees[0], 0, 0)] # cost, time, node

        for _from, _to, time in edges:
            adj_list[_from].append((_to, time))
            adj_list[_to].append((_from, time))

        while heap:
            fee, t, node = heapq.heappop(heap)

            for nei, nei_t in adj_list[node]:
                cand_t = t + nei_t
                if cand_t <= maxTime:
                    cand_fee = fee + passingFees[nei]
                    if cand_fee < fees[nei][cand_t]:
                        fees[nei][cand_t] = cand_fee
                        heapq.heappush(heap, (cand_fee, cand_t, nei))

        res = min(fees[N - 1])
        return res if res != float('inf') else -1