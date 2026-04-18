# https://leetcode.com/problems/maximum-matching-of-players-with-trainers

from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        n = len(players)
        m = len(trainers)
        players.sort()
        trainers.sort()
        i = 0
        j = 0
        count = 0

        while i < n and j < m:
            if players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1
        
        return count