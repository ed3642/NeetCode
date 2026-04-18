# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
import bisect
from collections import defaultdict

class Solution:
    # O(n)
    def countPalindromicSubsequence(self, s: str) -> int:
        
        # store the indexes of each letter
        # try to find a middle character between [left,...,...,...,right]
        # bisect for fast search

        char_pos = defaultdict(list)
        for i, c in enumerate(s):
            char_pos[c].append(i)
        
        count = 0
        for c, indexes in char_pos.items():
            left = indexes[0]
            right = indexes[-1]
            if left == right:
                continue
            for c2, indexes2 in char_pos.items():
                insert_i = bisect.bisect_left(indexes2, left + 1) # look for a number 1 bigger than left (i.e something in the middle of left and right)
                if insert_i < len(indexes2) and indexes2[insert_i] < right: # found something in the middle
                    count += 1
        
        return count

    # O(n)
    def countPalindromicSubsequence2(self, s: str) -> int:
        letters = set(s)
        count = 0

        for c in letters:
            left = s.index(c)
            right = s.rindex(c)
            if left == right:
                continue

            middle = set()
            for i in range(left + 1, right):
                middle.add(s[i])
            count += len(middle)
        
        return count

    def countPalindromicSubsequence3(self, s: str) -> int:
        
        N = len(s)
        left_state_at = [0] * N
        right_state_at = [0] * N
        bitmask = 0
        alphabet = set(s)
        letter_i = {c: i for i, c in enumerate(alphabet)}

        for i in range(N):
            activate_i = letter_i[s[i]]
            bitmask = bitmask | (1 << activate_i)
            left_state_at[i] = bitmask
        bitmask = 0
        for i in range(N - 1, -1, -1):
            activate_i = letter_i[s[i]]
            bitmask = bitmask | (1 << activate_i)
            right_state_at[i] = bitmask
        
        found = set()
        for i in range(1, N - 1):
            left = left_state_at[i - 1]
            right = right_state_at[i + 1]
            for pair_c in alphabet:
                pair_i = letter_i[pair_c]
                # needed bit turned on on both sides
                if (left & (1 << pair_i)) and (right & (1 << pair_i)): 
                    found.add(pair_c + s[i] + pair_c)
        
        return len(found)
    
s = Solution()
print(s.countPalindromicSubsequence("bbcbaba"))