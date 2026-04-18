# https://leetcode.com/problems/maximum-swap/
class Solution:
    def maximumSwap(self, num: int) -> int:
        def num_to_list(num):
            res = []
            while num:
                res.append(num % 10)
                num //= 10
            return list(reversed(res))

        if num < 10:
            return num
        tokens = num_to_list(num)
        N = len(tokens)
        first_find_from_right = [float('inf')] * 10
        first_find_from_right[tokens[-1]] = N - 1
        max_to_right = tokens.copy()
        for i in range(N - 2, -1, -1):
            max_to_right[i] = max(max_to_right[i + 1], max_to_right[i])
            if first_find_from_right[tokens[i]] == float('inf'):
                first_find_from_right[tokens[i]] = i

        for i in range(N):
            if max_to_right[i] > tokens[i]:
                swapping_i = first_find_from_right[max_to_right[i]]
                tokens[i], tokens[swapping_i] = tokens[swapping_i], tokens[i]
                return int(''.join([str(n) for n in tokens]))
        return num
