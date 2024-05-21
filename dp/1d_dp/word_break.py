from functools import lru_cache

class Solution:

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # if the last state is true and we can appended a word in the dict, mark this state as valid
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1) # account for empty string
        dp[0] = True # empty string

        for end in range(1, n + 1):
            for start in range(end):
                word = s[start:end]
                if dp[start] and word in word_set:
                    dp[end] = True
                    break
        
        return dp[n]

    # unnecessary dp calls
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # when we find a word, use to dp to take that word and not take it

        @lru_cache(maxsize=None)
        def dp(start, end):
            word = s[start:end + 1]

            if end == len(s) - 1:
                if word in word_set:
                    return True
                return False

            if word in word_set:
                take = dp(end + 1, end + 1)
                dont_take = dp(start, end + 1)

                return any([take, dont_take])
            else:
                return dp(start, end + 1) # dont take


        word_set = set(wordDict)

        return dp(0, 0)