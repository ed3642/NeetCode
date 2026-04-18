# https://leetcode.com/problems/sum-of-k-mirror-numbers

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        # gen base10 pals and check if base-k are also palindrones
        # gen pals from 1-9, then 10-99, then 100-999 etc..

        def check_base_k(num):
            # num % k peels off the right most digit in base k
            base_k = []
            while num > 0:
                base_k.append(str(num % k))
                num //= k
            digits = ''.join(base_k) #[::-1] dont need to reverse to get the actual order of the digits since we just care about the palindrone
            return digits == digits[::-1]

        _sum = 0
        count = 0
        is_odd_len = 1
        start = 1
        end = 10

        while count < n:
            if is_odd_len:
                for half in range(start // 10, end // 10):
                    half_str = str(half)
                    for mid in range(10):
                        mid_str = str(mid)
                        if half_str == '0':
                            half_str = ''
                        full = int(half_str + mid_str + half_str[::-1])
                        if full != 0 and check_base_k(full):
                            count += 1
                            _sum += full
                            if count == n:
                                return _sum
            else:
                for half in range(start // 10, end // 10):
                    half_str = str(half)
                    full = int(half_str + half_str[::-1])
                    if check_base_k(full):
                        count += 1
                        _sum += full
                        if count == n:
                            return _sum
            if is_odd_len:
                start *= 10
                end *= 10
            is_odd_len = (is_odd_len + 1) % 2

        return _sum