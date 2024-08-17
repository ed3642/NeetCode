class Solution:
    def validStrings(self, n: int) -> list[str]:
        
        def backtrack(builder: list):
            if len(builder) == n:
                res.append(''.join(builder))
                return
            
            builder.append('1')
            backtrack(builder)
            builder.pop()

            if len(builder) == 0 or builder[-1] == '1':
                builder.append('0')
                backtrack(builder)
                builder.pop()

        res = []
        backtrack([])
        return res
    
    def validStrings2(self, n: int) -> list[str]:
        
        def backtrack(builder: list):
            # Base case: if the builder length equals n, convert to string and add to results
            if len(builder) == n:
                res.append(''.join(map(str, builder)))
                return
            
            # Always allowed to add '1'
            builder.append(1)
            backtrack(builder)
            builder.pop()
            
            # Add '0' only if the last added was '1' (to ensure every pair has at least one '1')
            if len(builder) == 0 or builder[-1] == 1:
                builder.append(0)
                backtrack(builder)
                builder.pop()

        res = []
        backtrack([])
        return res
    
s = Solution()
print(s.validStrings(3))