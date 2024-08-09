# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        mappings = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(index, builder: list):
            if index >= len(digits):
                res.append(''.join(builder))
                return None
            
            for c in mappings[digits[index]]:
                builder.append(c)
                backtrack(index + 1, builder)
                builder.pop()
        
        if len(digits) == 0:
            return []
        res = []
        backtrack(0, [])
        return res