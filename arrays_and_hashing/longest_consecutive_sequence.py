class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        maxCount = 0
        hs = set(nums)
        hm = dict() # <num, chainLength>

        while hs:
            num = hs.pop()
            if not num in hm:
                hm[num] = 1
                # check chains to the right
                temp = num + 1
                while temp in hs:
                    hm[num] += 1
                    hs.remove(temp)
                    temp += 1
                # check chains to the left
                temp = num - 1
                while temp in hs:
                    hm[num] += 1
                    hs.remove(temp)
                    temp -= 1
            maxCount = max(maxCount, hm[num])

        return maxCount
             
    
s = Solution()

nums = [0,3,7,2,5,8,4,6,0,1,999999999]

print(s.longestConsecutive(nums))