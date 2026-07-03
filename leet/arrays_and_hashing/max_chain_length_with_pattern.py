# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset

from collections import defaultdict
from typing import Counter, List

class Solution:
    # best solution since chain lengths can only be 5, basically constant time chain completion
    def maximumLength(self, nums: List[int]) -> int:
        
        f = Counter(nums)
        max_size = 0

        if f[1] > 0:
            if f[1]%2 == 0:
                max_size = f[1]-1
            else:
                max_size = f[1]
            f[1] = 0
        
        for num in f:
            curr = num

            chain_size = 0
            while f[curr] > 1:
                if f[curr] >= 2:
                    # 2 new nums into chain
                    chain_size += 2
                curr = curr**2
            if f[curr] == 0:
                chain_size -= 1 # could not put in a peak, need to make prev num the peak so remove its partner and make it the peak
            else:
                chain_size += 1 # put in this curr as the peak
            max_size = max(chain_size, max_size)

        return max_size

    def maximumLength(self, nums: List[int]) -> int:
        
        f = Counter(nums)
        max_size = 0
        root_length = defaultdict(int)

        if f[1] > 0:
            if f[1]%2 == 0:
                max_size = f[1]-1
            else:
                max_size = f[1]
            f[1] = 0
        
        for num in f:
            curr = num

            chain_size = 0
            chain_already_processed = False
            while f[curr] > 1:
                if f[curr] >= 2:
                    # 2 new nums into chain
                    chain_size += 2
                    f[curr] -= 2
                curr = curr**2
                if curr in root_length:
                    chain_already_processed = True
                    root_length[num] = chain_size+root_length[curr]
                    max_size = max(root_length[num], max_size)
            # record end of chain
            if not chain_already_processed:
                if f[curr] == 0:
                    chain_size -= 1 # could not put in a peak, need to make prev num the peak so remove its partner and make it the peak
                else:
                    chain_size += 1 # put in this curr as the peak
                    f[curr] -= 1 
                root_length[num] = chain_size
                max_size = max(chain_size, max_size)

        return max_size
    
    def maximumLength(self, nums: List[int]) -> int:
        # sorts the counts, can make it not do that with a bit more memory
        
        f = Counter(nums)
        max_size = 0

        if f[1] > 0:
            if f[1]%2 == 0:
                max_size = f[1]-1
            else:
                max_size = f[1]
            f[1] = 0
        
        for num in sorted(f):
            curr = num

            chain_size = 0
            while f[curr] > 1:
                if f[curr] >= 2:
                    # 2 new nums into chain
                    chain_size += 2
                    f[curr] -= 2
                curr = curr**2
            if f[curr] == 0:
                chain_size -= 1 # could not put in a peak, need to make prev num the peak so remove its partner and make it the peak
            else:
                chain_size += 1 # put in this curr as the peak
                f[curr] -= 1 
            max_size = max(chain_size, max_size)

        return max_size