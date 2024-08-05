class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        
        def backtrack(i, builder):
            if len(builder) == len(digits):
                res.append(''.join(builder))

            if i >= len(digits):
                return
            
            num = digits[i]

            for j in range(i + 1, len(digits) + 1):
                for ch in mappings[num]:
                    builder.append(ch)
                    backtrack(j, builder)
                    builder.pop()
        
        if len(digits) == 0:
            return []

        res = []
        mappings = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        backtrack(0, [])
        return res
        