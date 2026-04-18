# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero
from typing import List

class Solution:
    # O(n * 24) = O(n), performs a bit better since the average bit length is smaller than 24
    def largestCombination(self, candidates: List[int]) -> int:
        # 100110001001011010000000, 24 bits max
        N = len(candidates)
        groups = [0] * 24
        for i in range(N):
            candidates[i] = bin(candidates[i])[2:]
            bits = candidates[i]
            length = len(bits)
            for i, bit in enumerate(bits):
                if bit == '1':
                    groups[length - i - 1] += 1

        return max(groups)
    
    # O(n * 24) = O(n)
    def largestCombination(self, candidates: List[int]) -> int:
        groups = [0] * 24
        for num in candidates:
            for i in range(24):
                if (num & (1 << i) != 0):
                    groups[i] += 1

        return max(groups)
    