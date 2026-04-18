class Solution:
    def sumDigitDifferences(self, nums: list[int]) -> int:
        str_nums = [str(num) for num in nums]  # convert numbers to strings
        total_diff = 0

        max_len = len(str_nums[0]) 

        for d in range(max_len):
            counts = [0] * 10
            for num in str_nums:
                counts[int(num[-d - 1])] += 1 
            for i in range(10):
                for j in range(i + 1, 10):
                    total_diff += counts[i] * counts[j] 

        return total_diff