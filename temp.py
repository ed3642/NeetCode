class Solution:
    def partition(self, s: str) -> list[list[str]]:
        
        def backtrack(start, builder):
            if start == len(s):
                res.append(builder.copy())
            
            if start >= len(s):
                return
            
            for end in range(start, len(s)):
                contiguous_section = s[start:end + 1]
                if is_pal(contiguous_section):
                    builder.append(contiguous_section)
                    backtrack(end + 1, builder)
                    builder.pop()

        def is_pal(string):
            return string == string[::-1]
        
        res = []
        backtrack(0, [])
        return res