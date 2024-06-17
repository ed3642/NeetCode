from collections import Counter, defaultdict
from functools import lru_cache

class Solution:

    # topdown -> bottomup from below
    def deleteAndEarn(self, nums: list[int]) -> int:
        _max = 0
        totals = defaultdict(int)
        for num in nums:
            totals[num] += num
            _max = max(_max, num)

        best = [0] * (_max + 1)
        best[1] = totals[1]

        for num in range(2, _max + 1):
            best[num] = max(
                best[num - 2] + totals[num],
                best[num - 1]
            )

        return best[_max]

    # get the max and consider each number from it
    def deleteAndEarn(self, nums: list[int]) -> int:
        
        @lru_cache(maxsize=None)
        def best(num):
            if num == 0:
                return 0
            if num == 1:
                return totals[1]
            
            return max(
                best(num - 2) + totals[num],
                best(num - 1),
            )

        _max = 0
        totals = defaultdict(int)
        for num in nums:
            totals[num] += num
            _max = max(_max, num)

        return best(_max)

    # nice solution
    def deleteAndEarn(self, nums: list[int]) -> int:
        max_nums = max(nums)
        total_worth = [0 for _ in range(max_nums + 1)]
        dp = [0] * len(total_worth)

        for num in nums:
            total_worth[num] += num

        dp[0] = total_worth[0]
        dp[1] = max(total_worth[0], total_worth[1])

        for i in range(2, len(total_worth)):
            dp[i] = max(dp[i - 1], dp[i - 2] + total_worth[i])

        return dp[len(total_worth) - 1]

    # O (nlogn)
    def deleteAndEarn2(self, nums: list[int]) -> int:
        nums.sort()
        frequencies = Counter(nums)

        options = []
        for num, count in frequencies.items():
            if not num - 1 in frequencies:
                options.append(0)
            options.append(num * count)
            if not num + 1 in frequencies:
                options.append(0)

        n = len(options)
        dp = [0] * n
        dp[0] = options[0]
        dp[1] = max(options[0], options[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + options[i], dp[i - 1])
        
        return dp[n - 1]
    
    # O (n)
    def deleteAndEarn3(self, nums: list[int]) -> int:
        # transform nums
        _max = max(nums)
        aggregate = [0] * (_max + 1) # index represents the number, v[i] is the total of that num

        for num in nums:
            aggregate[num] += num

        # dp section
        n = len(aggregate)
        if n == 1:
            return aggregate[0]
        elif n == 2:
            return max(aggregate[0], aggregate[1])
        
        dp = [0] * n
        dp[0] = aggregate[0]
        dp[1] = max(aggregate[0], aggregate[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], aggregate[i] + dp[i - 2])

        return max(dp[-1], dp[-2])
