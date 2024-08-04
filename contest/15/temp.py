from collections import defaultdict


class Solution:
    def winningPlayerCount(self, n: int, pick: list[list[int]]) -> int:
        picks = defaultdict(int)

        for player, ball in pick:
            picks[(player, ball)] += 1
        
        winners = set()
        for (player, _), same_count in picks.items():
            if same_count >= player + 1:
                winners.add(player)

        return len(winners)
    
s = Solution()
print(s.winningPlayerCount(n = 4, pick = [[0,0],[1,0],[1,0],[2,1],[2,1],[2,0]]))