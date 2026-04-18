class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        original_max = max(candies)
        res = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= original_max:
                res.append(True)
            else:
                res.append(False)
        
        return res