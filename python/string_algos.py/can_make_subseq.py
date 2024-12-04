# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        def can_transform(ch, ch2):
            ch_alphabet_i = (ord(ch) - ORD_ZERO + 1) % NUM_CHARS
            ord_i = ch_alphabet_i + ORD_ZERO
            
            if chr(ord_i) == ch2:
                return True
            return False

        if len(str1) < len(str2):
            return False
        
        ORD_ZERO = ord('a')
        NUM_CHARS = 26
        N = len(str2)
        i2 = 0

        for i in range(len(str1)):
            if str1[i] == str2[i2] or can_transform(str1[i], str2[i2]):
                i2 += 1
            if i2 == N:
                return True
        
        return False