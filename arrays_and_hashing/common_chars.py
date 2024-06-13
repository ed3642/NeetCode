from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        
        reduce = Counter(words[0])
        n = len(words)

        for i in range(1, n):
            curr_count = Counter(words[i])
            new_reduce = Counter()
            for ch, count in reduce.items():
                if ch in curr_count:
                    new_reduce[ch] = min(count, curr_count[ch])
            reduce = new_reduce
         
        res = []
        for ch, count in reduce.items():
            arr = ch * count
            res += arr
        return res