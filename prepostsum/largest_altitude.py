class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        curr_sum = 0
        max_sum = 0
        for num in gain:
            curr_sum += num
            max_sum = max(max_sum, curr_sum)

        return max_sum