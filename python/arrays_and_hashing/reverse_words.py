class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for word in reversed(s.split(' ')):
            if word != '':
                res.append(word)

        return ' '.join(res)