from functools import lru_cache

class Solution:

    def maxTotalReward2(self, rewardValues: list[int]) -> int:
        arr = sorted(list(set(rewardValues)))

        @lru_cache(maxsize=None)
        def max_val(i, total):
            if i >= len(arr):
                return 0
            else:
                leave = max_val(i + 1, total)
                if not arr[i] > total: # cant take
                    return leave
                take = arr[i] + max_val(i + 1, total + arr[i])

                return max(leave, take)

        return max_val(0, 0)

s = Solution()
print(s.maxTotalReward([1,1,3,3]))
print(s.maxTotalReward([1,6,4,3,2]))