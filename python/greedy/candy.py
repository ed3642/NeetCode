# https://leetcode.com/problems/candy

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        if N == 1:
            return 1
        
        candy = [1] * N

        for i in range(1, N):
            if ratings[i] > ratings[i - 1]:
                candy[i] = candy[i - 1] + 1
        for i in range(N - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i + 1] + 1, candy[i])

        return sum(candy)

    def candy(self, ratings: List[int]) -> int:

        # [0,1,2,1]

        # [1,1,1,1]
        # [1,2,1,1]
        # [1,2,3,1]
        
        N = len(ratings)
        if N == 1:
            return 1

        order = [(rating, i) for i, rating in enumerate(ratings)]
        order.sort(key=lambda x: x[0])
        candy = [1] * N

        for rating, i in order:
            if i == 0:
                # only look to right
                if ratings[i + 1] > rating:
                    candy[i + 1] = max(candy[i] + 1, candy[i + 1])
            elif i == N - 1:
                # only look to left
                if ratings[i - 1] > rating:
                    candy[i - 1] = max(candy[i] + 1, candy[i - 1])
            else:
                if ratings[i - 1] > rating:
                    candy[i - 1] = max(candy[i] + 1, candy[i - 1])
                if ratings[i + 1] > rating:
                    candy[i + 1] = max(candy[i] + 1, candy[i + 1])

        return sum(candy)
    