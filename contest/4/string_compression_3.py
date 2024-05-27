class Solution:
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
    
