class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        bitmask = 0
        bitmask_state_positions = {0: -1}
        bit_mappings = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        max_length = 0

        for i, c in enumerate(s):
            if c in bit_mappings:
                bitmask = bitmask ^ (1 << bit_mappings[c]) # toggle the corresponding bit to char
            if bitmask in bitmask_state_positions:
                max_length = max(i - bitmask_state_positions[bitmask], max_length)
            else:
                bitmask_state_positions[bitmask] = i
        
        return max_length