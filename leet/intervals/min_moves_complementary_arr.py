from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        
        # takes the cost function and subtract the 1 and 0 operation range modifications from it and then starting with a worst case of 2 ops for all sums it sees the min value of that cost func.
        # the cost function is 2 everywhere in the space at first and then we carve out improvements in it then check the min aftewards
        # 2 ops, [2, max(n1,n2)+limit]
        # 1 op, [min(n1+1,n2+1), max(n1,n2)+limit] => [min(n1,n2)+1, max(n1,n2)+limit]
        # 0 op, [n1+n2, n1+n2]

        n = len(nums)
        diff = [0] * (2 * limit + 2) # space of all possible sums we can try

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            # subtract sums to respective ranges
            l = min(a,b)+1
            r = max(a,b)+limit
            k = a+b

            # 1 op range [min(a,b)+1, max(a,b)+limit]
            diff[l] -= 1
            diff[r+1] += 1

            # 0 op range [k, k]
            diff[k] -= 1
            diff[k+1] += 1

        curr_ops = n # fill with worst case, all sums need 2 ops from each pair (1 op per num)
        min_ops = float('inf')

        for s in range(2, 2 * limit + 1):
            curr_ops += diff[s]
            min_ops = min(curr_ops, min_ops)

        return min_ops
