# https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/
 
class Solution:

    # O(n^2)
    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends == 1:
            return word
        
        n = len(word)
        biggest_i = 0
        for i, c in enumerate(word):
            if c > word[biggest_i]:
                biggest_i = i
        cand_i = []

        for i in range(n):
            if word[i] == word[biggest_i]:
                cand_i.append(i)
        
        # see longest part we can make with each cand_i

        max_size = n - numFriends + 1
        max_word = ''

        for i in cand_i:
            if i + max_size > n:
                # can only take to the end
                cand_word = word[i:]
                if cand_word > max_word:
                    max_word = cand_word
            else:
                # can take the max_size
                cand_word = word[i: i + max_size]
                if cand_word > max_word:
                    max_word = cand_word
        
        return max_word