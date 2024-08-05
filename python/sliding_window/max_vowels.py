class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiouAEIOU')

        max_count = 0
        count = 0
        n = len(s)

        for i in range(k):
            ch = s[i]
            if ch in vowels:
                count += 1
        max_count = count

        l = 0
        r = k
        for i in range(0, n - k):
            adding = s[r + i]
            leaving = s[l + i]
            if adding in vowels:
                count += 1
            if leaving in vowels:
                count -= 1
            max_count = max(max_count, count)

        return max_count 

