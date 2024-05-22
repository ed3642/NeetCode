class Solution:
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
