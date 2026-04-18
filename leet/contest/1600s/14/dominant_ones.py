# https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones
class Solution:
    # idk, really hard question
    # this is too slow
    def numberOfSubstrings(self, s: str) -> int:

        last_num_0 = 0
        last_num_1 = 0
        n = len(s)
        count = 0

        for end in range(1, n + 1):
            last_num_0 += 1 if s[end - 1] == '0' else 0
            last_num_1 += 1 if s[end - 1] == '1' else 0
            num_0 = last_num_0
            num_1 = last_num_1
            for start in range(end):
                length = end - start + 1
                if num_1 < length ** 0.5:
                    break
                if num_1 == 0:
                    break
                if num_0 * num_0 <= num_1:
                    count += 1
                if s[start] == '1':
                    num_1 -= 1
                else:
                    num_0 -= 1
        
        return count
    