from collections import deque

# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description/
class Solution:
    # this is a pretty general solution to the "min bit flips with window size K" problem.
    # NOTE: if the window size goes to the end of the array each flip, min_flips_2,py is a pretty clean solution in that case.
    def minKBitFlips(self, nums: list[int], k: int) -> int:
        # greedily try to flip each bit thats not a 1
        # keep track of effect of the bits that can effect the current bit

        n = len(nums)
        in_effect_queue = deque() # 0 means we didnt need to flip this bit, 1 means we flipped it
        needs_flip_state = 0 # 0 needs to be flipped, 1 do not flip
        flip_count = 0

        for i in range(n):

            # take off effect of expired bit
            if i >= k:
                needs_flip_state ^= in_effect_queue[0]

            if nums[i] == needs_flip_state:
                # if we need to flip a bit but the window is out of bounds, the problem is unsolvable
                if i + k > n:
                    return -1
                
                flip_count += 1
                in_effect_queue.append(1)
                needs_flip_state ^= 1
            else:
                in_effect_queue.append(0)
            
            # pop expired effect
            if len(in_effect_queue) > k:
                in_effect_queue.popleft()
        
        return flip_count
