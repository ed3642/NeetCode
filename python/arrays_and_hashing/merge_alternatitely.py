class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        def dump(string, i):
            while i < len(string):
                res.append(string[i])
                i += 1

        ptr1 = 0
        ptr2 = 0
        flag = True # which word to use
        res = []

        while ptr1 < len(word1) and ptr2 < len(word2):
            if flag:
                res.append(word1[ptr1])
                ptr1 += 1
            else:
                res.append(word2[ptr2])
                ptr2 += 1
            flag = not flag
        
        # dump the res of the remaining longer word
        if ptr1 == len(word1):
            dump(word2, ptr2)
        else:
            dump(word1, ptr1)
        
        return ''.join(res)