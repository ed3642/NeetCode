from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(start, builder, _sum):
            if _sum > n:
                return
            if len(builder) > k:
                return
            if _sum == n and len(builder) == k:
                res.append(builder.copy())
            
            for i in range(start, 10):
                builder.append(i)
                backtrack(i + 1, builder, _sum + i)
                builder.pop()

        res = []
        backtrack(1, [], 0)
        return res