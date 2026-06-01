# https://leetcode.com/problems/perfect-squares
from collections import deque
from functools import lru_cache
import math

class Solution:
    # O(n sqrt n)
    def numSquares(self, n: int) -> int:
        
        squares = [num * num for num in range(int(math.sqrt(n)) + 1)]

        q = deque([n])
        visited = [False] * (n + 1)
        visited[n] = True

        steps = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == 0:
                    return steps
                for s in squares:
                    nei = node - s
                    if nei >= 0 and not visited[nei]:
                        q.append(nei)
                        visited[nei] = True
            
            steps += 1
        
        return -1 # shouldnt happen

    def numSquares(self, n: int) -> int:
        
        @lru_cache(maxsize=None)
        def min_squares(num):
            if num == 0:
                return 0
            
            min_used = float('inf')
            for i in range(len(squares) - 1, -1, -1):
                next_num = num - squares[i]
                if next_num < 0:
                    continue
                min_used = min(min_squares(next_num) + 1, min_used)

            return min_used

        # generate squares from [1..n]
        squares = []
        curr_num = 1
        num_square = curr_num * curr_num

        while num_square <= n:
            squares.append(num_square)
            curr_num += 1
            num_square = curr_num * curr_num
        
        return min_squares(n)
    
    # O(n)
    # number theory solution
    # Lagrange’s Four-Square Theorem: every natural number can be represented as the sum of four integer squares. numSquares maps to [1,2,3,4]
    def numSquares(self, n: int) -> int:
        squares = set()
        curr_num = 1
        num_square = curr_num * curr_num
        while num_square <= n:
            squares.add(num_square)
            curr_num += 1
            num_square = curr_num * curr_num
        
        if n in squares:
            return 1
        for i in squares:
            if n - i in squares: return 2
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7: return 4
        return 3