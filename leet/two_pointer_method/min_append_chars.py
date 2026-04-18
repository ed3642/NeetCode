class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # process the ones that are there, append the ones we didnt find

        a = 0
        b = 0
        s_len = len(s)
        t_len = len(t)

        while a < s_len and b < t_len:
            if s[a] == t[b]:
                b += 1
            a += 1

        need = t_len - b

        return need