from collections import deque

class Solution:

    # O(n)
    def findWinningPlayer(self, skills: list[int], k: int) -> int:

        n = len(skills)
        winner = 0
        winner_streak = 0

        for opponent in range(1, n):
            if skills[opponent] > skills[winner]:
                winner = opponent
                winner_streak = 1
            else:
                winner_streak += 1
            if winner_streak >= k:
                return winner
        return winner

    def findWinningPlayer2(self, skills: list[int], k: int) -> int:
        
        n = len(skills)
        queue = deque(zip([i for i in range(n)], skills))
        
        winner_streak = 0

        while True:
            p1, p1_skill = queue.popleft() # last winner
            p2, p2_skill = queue.popleft() # opponent

            if p1_skill < p2_skill:
                queue.append((p1, p1_skill))
                queue.appendleft((p2, p2_skill))
                winner_streak = 1
            else:
                queue.append((p2, p2_skill))
                queue.appendleft((p1, p1_skill))
                winner_streak += 1

            if winner_streak >= k or winner_streak >= n:
                return queue[0][0]


s = Solution()
print(s.findWinningPlayer([1,2,3], 1))