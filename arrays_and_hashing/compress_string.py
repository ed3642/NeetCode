class Solution:
    def compress(self, chars: list[str]) -> int:
        def write(writting_i, last_char, streak):
            if streak == 1:
                chars[writting_i] = last_char
                writting_i += 1
            else:
                chars[writting_i] = last_char
                streak_string = str(streak)
                writting_i += 1
                if len(streak_string) > 1:
                    for ch in streak_string:
                        chars[writting_i] = ch
                        writting_i += 1
                else:
                    chars[writting_i] = str(streak)
                    writting_i += 1
            return writting_i

        last_char = chars[0]
        n = len(chars)
        i = 0
        writting_i = 0
        streak = 0

        while i < n:
            ch = chars[i]
            if chars[i] == last_char:
                streak += 1
            else:
                i -= 1
                writting_i = write(writting_i, last_char, streak)
                streak = 0
            last_char = ch
            i += 1
        
        writting_i = write(writting_i, last_char, streak)

        return writting_i