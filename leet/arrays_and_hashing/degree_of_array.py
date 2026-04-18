from collections import defaultdict

class Solution:
    # O(n)
    def findShortestSubArray(self, nums: list[int]) -> int:
        freqs = defaultdict(int) # freq, len, first_left

        for i, num in enumerate(nums):
            if num not in freqs:
                freqs[num] = [1, 1, i]
            else:
                freqs[num][0] += 1
                freqs[num][1] = i - freqs[num][2] + 1
        
        max_freq_num = None
        max_freq_len = 1
        max_freq = 0
        for key, item in freqs.items():
            freq = item[0]
            length = item[1]
            if freq > max_freq:
                max_freq = freq
                max_freq_len = length
                max_freq_num = key
            elif freq == max_freq and length < max_freq_len:
                max_freq = freq
                max_freq_len = length
                max_freq_num = key

        return freqs[max_freq_num][1] 