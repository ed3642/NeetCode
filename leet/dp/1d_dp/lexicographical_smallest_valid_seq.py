from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:

        # this problem was pretty hard, couldnt see without hints that you had to make a dp array to greedly make choice later

        # bacdc abc
        # 1 1 1 1 0
        N = len(word1)
        M = len(word2)
        res = [0] * M

        # Suffix Makeable of word2 starting at i of word1
        sfm = [0] * (N+1)

        for i in range(N-1, -1, -1):
            if word1[i] == word2[M-1-sfm[i+1]]:
                sfm[i] = sfm[i+1]+1
            else:
                sfm[i] = sfm[i+1]
            if sfm[i] == M:
                # can make the whole word2 from here
                for j in range(i, -1, -1):
                    sfm[j] = M
                break

        pfm = 0 # Prefix Makeable
        j = 0
        for i in range(N):
            # can complete word2
            sf = sfm[i+1] if i+1 < N else 0
            if pfm + sf >= M-1:
                change_used = False
                for k in range(i, N):
                    if word1[k] == word2[j]:
                        res[j] = k
                        j += 1
                        if j == M:
                            break
                    elif not change_used:
                        change_used = True
                        res[j] = k # put wild card here
                        j += 1
                    if j == M:
                        return res
                return res
            if word1[i] == word2[j]:
                res[j] = i
                pfm += 1
                j += 1

        return []
