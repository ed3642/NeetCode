from collections import Counter

class Solution:
    # O (nlogn)
    def deleteAndEarn(self, nums: list[int]) -> int:
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
    def deleteAndEarn(self, nums: list[int]) -> int:
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
