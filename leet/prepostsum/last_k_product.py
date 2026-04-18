# https://leetcode.com/problems/product-of-the-last-k-numbers/
class ProductOfNumbers:

    #   [2,5,4]
    # [1,2,10,40]

    def __init__(self):
        self.last_zero_dist = float('inf')
        self.pf_nums = [1] # positive nums product prefix after last zero, 1 is the stub

    # O(1)
    def add(self, num: int) -> None:
        if num == 0:
            self.pf_nums = [1]
            self.last_zero_dist = 0
            return
        self.pf_nums.append(self.pf_nums[-1] * num)
        self.last_zero_dist += 1

    # O(1)
    def getProduct(self, k: int) -> int:
        if k > self.last_zero_dist:
            return 0
        return self.pf_nums[-1] // self.pf_nums[-(k + 1)]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)