# https://leetcode.com/problems/sort-vowels-in-a-string

class Solution:
    def sortVowels(self, s: str) -> str:
        # counting sort

        n = len(s)
        vowels = 'AEIOUaeiou'
        freq = {c: 0 for c in 'AEIOUaeiou'}
        res = [c for c in s]
        original_indexes = []

        for i in range(n):
            if s[i] in freq:
                freq[s[i]] += 1
                original_indexes.append(i)
        
        placing_i = 0
        for c in vowels:
            while freq[c] > 0:
                res[original_indexes[placing_i]] = c
                freq[c] -= 1
                placing_i += 1
        
        return ''.join(res)

    def sortVowels(self, s: str) -> str:
        
        n = len(s)
        vowels = set('aeiouAEIOU')
        res = [c for c in s]
        vowel_positions = []

        for i in range(n):
            if s[i] in vowels:
                vowel_positions.append((s[i], i))
        
        sorted_vowels = sorted(vowel_positions, key=lambda x: x[0])

        for i in range(len(sorted_vowels)):
            original_i = vowel_positions[i][1]
            res[original_i] = sorted_vowels[i][0]
        
        return ''.join(res)

s = Solution()
print(s.sortVowels(s = "lEetcOde"))