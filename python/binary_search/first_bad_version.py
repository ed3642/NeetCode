# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    # NOTE: theres always atleast 1 bad version
    def firstBadVersion(self, n: int) -> int:
        if n == 1: 
            return n

        l = 1
        r = n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        
        return l
