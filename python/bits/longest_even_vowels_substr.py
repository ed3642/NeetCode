class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # bitmask represention parity of vowels and store position of seen states
        # the string from first state encounter to curr same state encounter is a valid string

        N = len(s)
        bitmask = 0 # uoiea, the vowels backwards since 1 is 00..001 in binary
        bit_positions = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        state_positions = {0: -1}
        max_length = 0

        for i in range(N):
            if s[i] in bit_positions:
                bitmask = bitmask ^ (1 << bit_positions[s[i]]) # toggles the bit in this vowels position

            if bitmask in state_positions:
                max_length = max(i - state_positions[bitmask], max_length)
            else:
                state_positions[bitmask] = i
        
        return max_length
