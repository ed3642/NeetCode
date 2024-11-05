class Solution:
    def compressedString(self, word: str) -> str:
        
        res = []
        streak = 0
        for i in range(1, len(word)):
            streak += 1 
            if word[i] == word[i - 1]:
                if streak == 9:
                    res.append(str(streak))
                    res.append(word[i])
                    streak = 0
            else:
                res.append(str(streak))
                res.append(word[i - 1])
                streak = 0
        res.append(str(streak + 1))
        res.append(word[-1])

        return ''.join(res)

    def compressedString(self, word: str) -> str:

        def add_compression(count, ch):
            repeat = count // 9
            repeat_str = f'9{ch}' * repeat
            rest = count % 9
            rest_str = str(rest) + ch

            res.append(repeat_str)
            if rest > 0:
                res.append(rest_str)
        
        res = []
        count = 0
        last = word[0]
        for ch in word:
            if ch == last:
                count += 1
            else: # append
                add_compression(count, last)
                count = 1
            last = ch

        # add missing end
        add_compression(count, last)

        return ''.join(res)
    
