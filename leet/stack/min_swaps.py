# https://leetcode.com/problems/separate-black-and-white-balls/description/
class Solution:
    # NOTE: there is a one pass solution with two pointers
    def minimumSteps(self, s: str) -> int:
        
        # 1100011

        N = len(s)
        num_ones = 0
        ones_pos_stack = []
        for i, c in enumerate(s):
            if c == '1':
                num_ones += 1
                ones_pos_stack.append(i)
        
        total = 0
        ones_boundary = N - 1 - num_ones
        # dont use ones already in place
        while ones_pos_stack and ones_pos_stack[-1] > ones_boundary:
            ones_pos_stack.pop()

        for i in range(N - 1, ones_boundary, -1):
            if not ones_pos_stack:
                break
            if s[i] == '0':
                closest_one_index = ones_pos_stack.pop()
                total += i - closest_one_index

        return total
    