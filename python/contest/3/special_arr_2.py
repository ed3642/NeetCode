class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        # build valid ranges
        # check if query is in a valid range

        n = len(nums)
        valid_ranges = []

        # preprocess
        for i, num in enumerate(nums):
            nums[i] = num % 2

        l = 0
        r = 1

        while r < n:
            par1 = nums[r - 1]
            par2 = nums[r]

            if par1 == par2:
                valid_ranges.append([l, r - 1])
                l = r
                r = l + 1
                while r < n and nums[l] == nums[r]:
                    l += 1
                    r += 1

            if r < n:
                r += 1

        # close last interval
        valid_ranges.append([l, r - 1])

        # farthest each elem can reach with maintaining req
        farthest = [i for i in range(len(nums))]

        for _from, to in valid_ranges:
            for i in range(_from, to + 1):
                farthest[i] = to
                
        # print(farthest)
        # print(nums)
        # print(valid_ranges)

        res = []
        for _from, to in queries:
            if _from == to:
                res.append(True)
                continue
            if farthest[_from] == farthest[to]:
                res.append(True)
            else:
                res.append(False)

        return res