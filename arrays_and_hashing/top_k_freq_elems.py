from collections import Counter

class Solution:
    # assume k is always valid [1, unique elems in nums]
    # just saw Counter has a built in func for this but we can do it ourselfs
    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
        freqs = Counter(nums)
        return list(item[0] for item in freqs.most_common(k))
    

s = Solution()

nums = [1,1,1,2,2,3]

print(s.topKFrequent(nums, 2))