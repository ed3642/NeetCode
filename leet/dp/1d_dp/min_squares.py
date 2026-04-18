# https://leetcode.com/problems/perfect-squares
from functools import lru_cache

class Solution:
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