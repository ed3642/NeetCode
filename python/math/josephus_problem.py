# https://leetcode.com/problems/find-the-winner-of-the-circular-game

class Solution:
    # O(n)
    def findTheWinner(self, n: int, k: int) -> int:
        # Josephus problem
        # f(n,k) = (f(n - 1, k) + k) % n
        # we add + k to shift the indexes back to the previous states indexing
        # we do % n to give the indexing the circular looping behavior  
        def find_winner(n, k):
            if n == 1:
                return 0
            return (find_winner(n - 1, k) + k) % n

        return find_winner(n, k) + 1

    # O(n*k)
    def findTheWinner(self, n: int, k: int) -> int:
        
        queue = deque([i for i in range(1, n + 1)])

        streak = 0
        while len(queue) > 1:
            curr = queue.popleft()
            streak += 1
            if streak < k:
                queue.append(curr)
            else:
                streak = 0

        return queue[0]