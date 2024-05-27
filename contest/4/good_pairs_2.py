from collections import defaultdict

class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        
        count = 0
        nums2_processed_freqs = defaultdict(int) # freq of results
        for num in nums2:
            key = num * k
            nums2_processed_freqs[key] += 1

        for num in nums1:
            for divisor in range(1, int(num ** 0.5) + 1):
                if num % divisor == 0:
                    count += nums2_processed_freqs[divisor]

                    if divisor != num // divisor: # num // divisor is the pair when divisor is greater than int(num ** 0.5)
                        count += nums2_processed_freqs[num // divisor]

        return count