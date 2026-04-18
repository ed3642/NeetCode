class Solution:
    def reverseVowels(self, s: str) -> str:
        # make a list of each vowel in a stack

        vowels = []
        vowels_set = set('aeiuoAEIOU')

        for ch in s:
            if ch in vowels_set:
                vowels.append(ch)

        builder = []
        for i, ch in enumerate(s):
            if ch in vowels_set:
                builder.append(vowels.pop())
            else:
                builder.append(s[i])

        return ''.join(builder)