# there is a way to do it in O(1) space recursively
from typing import List

class Solution:
    # O(n) time O(lg n) space
    def lexicalOrder(self, n: int) -> List[int]:
        
        def dfs(prev, curr):
            cand = prev + curr
            res.append(int(cand))
            for i in range(10):
                if int(cand + str(i)) > n:
                    return
                dfs(cand, str(i))

        res = []

        for i in range(1, min(10, n + 1)):
            dfs(str(i), '')

        return res