class Solution:
    def partition(self, s: str) -> list[list[str]]:
        
        def backtrack(start, builder):
            if start >= len(s):
                partitions.append(builder.copy())
                return

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word == word[::-1]:
                    builder.append(word)
                    backtrack(end, builder)
                    builder.pop()

        partitions = []
        backtrack(0, [])
        return partitions
    
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

    def partition(self, s: str) -> list[list[str]]:

        def backtrack(start, builder):
            if start == len(s):
                res.append(builder.copy())

            for end in range(start, len(s)):
                candidate = s[start:end + 1]
                if is_pal(candidate):
                    builder.append(candidate)
                    backtrack(end + 1, builder)
                    builder.pop()

        def is_pal(string):
            return string == string[::-1]

        res = []
        backtrack(0, [])
        return res
