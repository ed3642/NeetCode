import itertools

class Solution:
    # practical way
    def combine1(self, n: int, k: int) -> list[list[int]]:
        return list(itertools.combinations(range(1, n + 1), k))
    
    # backtracking
    def combine(self, n: int, k: int) -> list[list[int]]:

        def backtrack(start, builder):
            if len(builder) == k:
                combs.append(builder.copy())
                return
            
            for num in range(start, n + 1):
                builder.append(num)
                backtrack(num + 1, builder)
                builder.pop()


        combs = []
        backtrack(1, [])
        return combs