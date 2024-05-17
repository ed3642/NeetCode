class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        
        def backtrack(num, total, builder):

            if len(builder) > k:
                return

            if total == n and len(builder) == k:
                res.append(builder.copy())
            
            for num in range(num + 1, 10):
                builder.append(num)
                backtrack(num, total + num, builder)
                builder.pop()

        res = []
        backtrack(0, 0, [])
        return res