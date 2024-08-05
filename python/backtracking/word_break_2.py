class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        # make all possible combinations of words from the string

        def backtrack(start, builder):
            
            if start == len(s):
                sentences.append(builder.copy())

            if start >= len(s):
                return
            
            for end in range(start, len(s)):
                word = s[start:end + 1]
                if word in words_set:
                    builder.append(word)
                    backtrack(end + 1, builder)
                    builder.pop()
        
        sentences = []
        words_set = set(wordDict)
        res = []
        backtrack(0, [])
        for sentence in sentences:
            res.append(' '.join(sentence))
        return res