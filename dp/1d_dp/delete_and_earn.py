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
        max_num = max(nums)
        frequencies = [0] * (max_num + 1)

        for num in nums:
            frequencies[num] += 1
        
        options = [0] * (max_num + 1)
        for i, freq in enumerate(frequencies):
            options[i] = i * freq

        n = len(options)
        dp = [0] * n
        dp[0] = options[0]
        dp[1] = max(options[0], options[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + options[i], dp[i - 1])
        
        return dp[n - 1]