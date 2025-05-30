class Solution:
    def __init__(self):
        self.memo = [-1] * 10001 # -1, 0, 1

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        # could also use digit dp for better solution

        count = 0
        
        for num in range(max(low, 11), high + 1):
            if self.memo[num] == 1:
                count += 1
            elif self.memo[num] == -1:
                num_int_arr = [int(val) for val in str(num)]
                if len(num_int_arr) % 2 != 0:
                    self.memo[num] = 0
                    continue
                mid = len(num_int_arr) // 2
                first_half = sum(num_int_arr[:mid])
                second_half = sum(num_int_arr[mid:])
                if first_half == second_half:
                    count += 1 # new value one
                    self.memo[num] = 1
                else:
                    self.memo[num] = 0
        
        return count
