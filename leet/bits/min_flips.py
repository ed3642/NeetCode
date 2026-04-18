# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal

        return sum(1 for c in bin(xor) if c == '1')
    
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal

        return bin(xor).count('1')
    