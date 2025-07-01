# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k

from functools import lru_cache

class Solution:

    # O(n) optimal
    def longestSubsequence(self, s: str, k: int) -> int:

        n = len(s)
        i = n - 1
        num = 0
        length = 0

        # take as much from the right side
        while num <= k and i >= 0:
            if s[i] == '1':
                if num + (1 << length) > k:
                    break
                num += 1 << length
            length += 1
            i -= 1

        # include 0s before the start of the taken right side
        for j in range(i):
            if s[j] == '0':
                length += 1
        
        return length

    # O(n)
    def longestSubsequence(self, s: str, k: int) -> int:
        # greedily take and drop leftmost 1 when cant take

        def left_most_bit_val(num):
            if num == 0:
                return 0
            return 1 << (num.bit_length() - 1)

        max_lenth = 0
        length = 0
        num = 0

        for i in range(len(s)):
            if s[i] == '0':
                # drop 1s until we can take this 0
                while num << 1 > k:
                    num = num - left_most_bit_val(num)
                    length -= 1
                num <<= 1
            else:
                # drop 1s until we can take this 1
                while (num << 1) + 1 > k:
                    num = num - left_most_bit_val(num)
                    length -= 1
                num = (num << 1) + 1
            length += 1
            max_lenth = max(length, max_lenth)

        return max_lenth

    # O(n log n)
    def longestSubsequence(self, s: str, k: int) -> int:
        # greedily take and drop leftmost 1 when cant take

        def left_most_bit_val(num):
            if num == 0:
                return 0
            val = 1
            while num > 1:
                num >>= 1
                val <<= 1
            return val

        max_lenth = 0
        length = 0
        num = 0

        for i in range(len(s)):
            if s[i] == '0':
                # drop 1s until we can take this 0
                while num << 1 > k:
                    num = num - left_most_bit_val(num)
                    length -= 1
                num <<= 1
            else:
                # drop 1s until we can take this 1
                while (num << 1) + 1 > k:
                    num = num - left_most_bit_val(num)
                    length -= 1
                num = (num << 1) + 1
            length += 1
            max_lenth = max(length, max_lenth)

        return max_lenth

    # MLE
    def longestSubsequence(self, s: str, k: int) -> int:
        
        @lru_cache(maxsize=None)
        def longest(i, num):
            if i >= len(s):
                return 0
            if num > k:
                return 0
            
            if s[i] == '0':
                cand = num << 1
                if cand <= k:
                    return longest(i + 1, cand) + 1
                return 0

            # s[i] == '1'
            op1 = 0
            cand = (num << 1) + 1
            if cand <= k:
                op1 = longest(i + 1, cand) + 1
            op2 = longest(i + 1, num)
            return max(op1, op2)
        
        return longest(0, 0)
    