# https://leetcode.com/problems/lexicographical-numbers

from typing import List

class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        
        num = 1
        res = []

        for _ in range(n):
            res.append(num)
            if num * 10 <= n:
                num *= 10
            else:
                while num % 10 == 9 or num + 1 > n:
                    num //= 10
                num += 1
        
        return res

    # works but not O(1) space
    def lexicalOrder(self, n: int) -> List[int]:

        def bt(builder):     
            res.append(builder)
            
            for nei in range(10):
                builder = builder * 10 + nei
                if builder > n:
                    break
                bt(builder)
                builder //= 10

        res = []

        for num in range(1, min(n + 1, 10)):
            bt(num)

        return res